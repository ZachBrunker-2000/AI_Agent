import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        working_directory_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory,file_path or "."))
        
        if not abs_file_path.startswith(working_directory_path):
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.exists(abs_file_path):
            return(f'Error: File "{file_path}" not found.')
        if not file_path.endswith('.py'):
            return(f'Error: "{file_path}" is not a Python file.')
        
        result = subprocess.run(["python3", abs_file_path],capture_output=True,timeout=30,text=True)
        print(result.stdout)
        print(result.stderr)
    except PermissionError:
        return f'Error: You do not have Permission to execute {file_path}.'   
        
    except OSError as e:
        return f"Error: {e}"