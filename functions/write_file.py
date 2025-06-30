import os
import errno

def write_file(working_directory, file_path, content):
    
    try:
        working_directory_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory,file_path or "."))
        file_directory_path = os.path.dirname(abs_file_path)
        
        if not abs_file_path.startswith(working_directory_path):
            
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

        if not os.path.exists(file_directory_path):
            os.makedirs(file_directory_path)
            
        
        with open(abs_file_path,"w") as f:
            f.write(content)
        
        return f'Sucessfully wrote to "{file_path}" ({len(content)} characters written)'
    except PermissionError:
        return f'Error: You do not have permission for {file_path}'
    except OSError as e:
            return (f'Error: {e}')
        