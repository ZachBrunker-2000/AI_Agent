import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

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

system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

messages = [
    types.Content(role="user", parts=[types.Part(text=content)]),
]


response = client.models.generate_content(
    model=model, 
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

if verbose:
    print(f"User prompt: {content}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(f"\n{response.text}")
