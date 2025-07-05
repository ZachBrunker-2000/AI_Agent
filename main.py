import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a specified file, truncated to 1000 chars",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_name": types.Schema(
                type=types.Type.STRING,
                description="The file name to get the content"
            )
        }
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a python program on the specified file path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the python executable to be ran"
            )
        }
    )
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file on the specified file path. Will create a new file if one does not exist at the specified location",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to be written"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the specified file"
            )
        }
    )
)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

verbose = False

if len(sys.argv) == 1:
    print("Error: missing prompt...")
    sys.exit(1)

if "-v" in sys.argv or "--verbose" in sys.argv:
    verbose = True
    
model = "gemini-2.0-flash-001"
content = sys.argv[1]

max_loops = 20



available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part,verbose=False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else: 
        print(f" - Calling function: {function_call_part.name}")
        
    function_map = {
        "get_files_info":get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file
    }
        
    function_call_part.args["working_directory"] = "./calculator"
    
    func = function_map.get(function_call_part.name)
    if func is None:
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"unknown function: {function_call_part.name}"},
                    )
                ],
            ) 
    else:
        result = func(**function_call_part.args) 
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": result},
                    )
                ],
            )
         
            
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
- you have access to tools to explore files
- Use get_files_info to see what files are available
- Use get_file_content to read specific files
- If a file acessed with get_file_content isn't relevent, try another file
- Create and list a plan on how you intend to resolve the users request
- when listing what function you are calling also include the arguments for that function call

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

messages = [
    types.Content(role="user", parts=[types.Part(text=content)]),
]

response = client.models.generate_content(
    model=model, 
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
)

i = 1
ongoing = True
func_exist = False

while ongoing:
    func_exist = False
    response = client.models.generate_content(
            model=model,
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
        )
    
    for i, candidate in enumerate(response.candidates):
        for j, part in enumerate(candidate.content.parts): 
            if hasattr(part, 'function_call'):
                if bool(part.function_call):
                    messages.append(candidate.content)
                    func_exist = True
                    func_result = call_function(part.function_call, verbose)
                    messages.append(func_result)
                    
            
    if not func_exist:
        print(response.text)
        break
    
    i += 1
    
    
    if i == 20:
        print(response.text)
        break
    



    
    