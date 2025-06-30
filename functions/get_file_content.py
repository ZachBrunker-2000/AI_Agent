import os


def get_file_content(working_directory, file_name):
    
    MAX_CHARS = 10000
    is_large_file = False
    working_directory_path = os.path.abspath(working_directory)
    file_path = os.path.abspath(os.path.join(working_directory,file_name or "."))
        
    if not file_path.startswith(working_directory_path) and file_path != working_directory_path:
        return (f'Error: Cannot read "{file_name}" as it is outside the permitted working directory')
    if not os.path.isfile(file_path):
        return (f'Error: "{file_name}" is not a file')
    
    with open(file_path,"r") as f:
        file_content_string = f.read(MAX_CHARS)
        
        if len(file_content_string) >= 10000:
            is_large_file = True
    
    if is_large_file:
        return f'{file_content_string}... \n"{file_name}" truncated at 10000 characters'
    
    return f"{file_content_string}."