import os


def get_files_info(working_directory, directory = None):
    #directory = directory or "."
    file_list=[]
    working_directory_path = os.path.abspath(working_directory)
    dir_path = os.path.abspath(os.path.join(working_directory,directory or "."))
    if not dir_path.startswith(working_directory_path) and dir_path != working_directory_path:
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    elif not os.path.isdir(dir_path):
        return (f'Error: "{directory}" is not a directory')
    
    for file in os.listdir(dir_path):
            file_list.append(f"-{file}: file_size={os.path.getsize(os.path.join(working_directory_path,directory,file))} bytes, is_dir={os.path.isdir(os.path.join(working_directory_path,directory,file))}\n")
            
            
    return "\n".join(file_list)