import os
import shutil
import time


def touch(File_Name):
    try:
        if not os.path.isfile(File_Name):
            with open(File_Name, 'w') as f:
                pass
        return f"File {File_Name} created successfully."
    except Exception as e:
        return f"An error occurred while creating the file: {e}"
    

def cat(File_Name):
    try:
        with open(File_Name, 'r') as f:
            read = f.read()
        return read
    except FileNotFoundError:
        return f"The file {File_Name} does not exist."
    except PermissionError:
        return f"Permission denied to read the file {File_Name}."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

def nano(File_Name, Mode, Write):
    try:
        File = str(File_Name)
        Mode = str(Mode)
        with open(File, Mode) as file:
            file.write(f'{Write}')
        return f"File written successfully: {File_Name}"
    except FileNotFoundError:
        return f"The file {File_Name} does not exist."
    except PermissionError:
        return f"Permission denied to write to the file {File_Name}."
    except Exception as e:
        return f"An error occurred while writing to the file: {e}"

def rm(File_Name):
    try:
        if os.path.isfile(File_Name):
            os.remove(File_Name)
            return f"File {File_Name} removed successfully."
        else:
            return f"The file {File_Name} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def mkdir(Folder_Name):
    try:
        if not os.path.isdir(Folder_Name):
            os.mkdir(Folder_Name)
            return f"Folder {Folder_Name} created successfully."
        else:
            return f"The folder {Folder_Name} already exists."
    except Exception as e:
        return f"An error occurred: {e}"

def rmdir(Folder_Name):
    try:
        if os.path.isdir(Folder_Name):
            os.rmdir(Folder_Name)
            return f"Folder {Folder_Name} removed successfully."
        else:
            return f"The folder {Folder_Name} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def ren(Name, New_Name):
    try:
        os.rename(Name, New_Name)
        return f"{Name} was renamed to {New_Name} successfully."
    except FileNotFoundError:
        return f"The {Name} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def mv(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        return f"Moved {source_path} to {destination_path} successfully."
    except FileNotFoundError:
        return f"The source path {source_path} does not exist."
    except PermissionError:
        return f"Permission denied to move {source_path} to {destination_path}."
    except Exception as e:
        return f"An error occurred: {e}"

def cd(path):
    try:
        os.chdir(path)
        return f"Changed directory to: {os.getcwd()}"
    except FileNotFoundError:
        return f"The directory {path} does not exist."
    except PermissionError:
        return f"Permission denied to change directory to {path}."
    except Exception as e:
        return f"An error occurred: {e}"

def tree(chomain):
    result = []
    for root, dirs, files in os.walk(chomain):
        result.append(f'Root: {root}')
        for dir_name in dirs:
            result.append(f'   Directory: {os.path.join(root, dir_name)}')
        for file_name in files:
            result.append(f'   File: {os.path.join(root, file_name)}')
    return '\n'.join(result)

def pwd():
    return os.getcwd()

def ls(path):
    result = []
    try:
        dir1 = os.listdir(path)
        for item in dir1:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            item_type = 'Directory' if is_dir else 'File'
            result.append(f"{item_type}: {item}")
    except FileNotFoundError:
        return f"Path {path} does not exist."
    except PermissionError:
        return f"Permission denied to list contents of {path}."
    except Exception as e:
        return f"An error occurred: {e}"
    return '\n'.join(result)

def ls_l(path):
    result = []
    try:
        dir1 = os.listdir(path)
        for item in dir1:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path)
            last_modified = time.ctime(os.path.getmtime(item_path))
            item_type = 'Directory' if is_dir else 'File'
            result.append(f"{item_type}: {item}")
            result.append(f"    Size: {size} bytes")
            result.append(f"    Last Modified: {last_modified}")
    except FileNotFoundError:
        return f"Path {path} does not exist."
    except PermissionError:
        return f"Permission denied to list contents of {path}."
    except Exception as e:
        return f"An error occurred: {e}"
    return '\n'.join(result)

def istime(path_Name):
    try:
        stat = os.stat(path_Name).st_atime
        st_time = time.ctime(stat)
        return f"Last access time of {path_Name}: {st_time}"
    except FileNotFoundError:
        return f"The file {path_Name} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def size(path_Name):
    try:
        size = os.stat(path_Name).st_size
        return f"Stat size of {path_Name}: {size} bytes"
    except FileNotFoundError:
        return f"The file {path_Name} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def get_info():
    result = []
    for key, value in os.environ.items():
        result.append(f"{key} : {value}")
    return '\n'.join(result)

def get_path():
    result = []
    path = os.get_exec_path()
    result.append(f"Executable paths:")
    for p in path:
        result.append(f"path: {p}")
    return '\n'.join(result)

