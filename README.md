# osManag

`osManag`(Operating System Management) is a Python library for managing files and folders easily and quickly. The library includes multiple functions for creating, reading, writing, and deleting files and folders, as well as changing directories and listing directory contents.

#### Functions

Here’s a description of each function in the `osManang` module:

1. **`touch(File_Name)`**
   - **Description:** Creates an empty file if it does not already exist.
   - **Usage:**
     ```python
     #Examples 1:
     osManang.touch('filename.txt')
     #Examples 2:
     File = osManang.touch('filename.txt')
     print(File)
     ```

2. **`cat(File_Name)`**
   - **Description:** Reads and returns the contents of the specified file.
   - **Usage:**
     ```python
     #Examples 1:
     content = osManang.cat('filename.txt')
     print(content)
     ```

3. **`nano(File_Name, Mode, Write)`**
   - **Description:** Writes content to a file. The mode can be 'w' (write) or 'a' (append).
   - **Usage:**
     ```python
     #Examples 1:
     osManang.nano('filename.txt', 'w', 'Hello, World!')
     #Examples 2:
     File = osManang.nano('filename.txt', 'w', 'Hello, World!')
     print(File)
     ```

4. **`rm(File_Name)`**
   - **Description:** Deletes the specified file.
   - **Usage:**
     ```python
     #Examples 1:
     osManang.rm('filename.txt')
     #Examples 2:
     File = osManang.rm('filename.txt')
     print(File)
     ```

5. **`mkdir(Folder_Name)`**
   - **Description:** Creates a new folder if it does not already exist.
   - **Usage:**
     ```python
     #Examples 1:
     osManang.mkdir('foldername')
     #Examples 2:
     File = osManang.mkdir('foldername')
     print(File)
     ```

6. **`rmdir(Folder_Name)`**
   - **Description:** Deletes the specified folder.
   - **Usage:**
     ```python
     #Examples 1:
     osManang.rmdir('foldername')
     #Examples 2:
     File = osManang.rmdir('foldername')
     print(File)
     ```

7. **`ren(Name, New_Name)`**
   - **Description:** Renames a file or folder from `Name` to `New_Name`.
   - **Usage:**
     ```python
     #Examples 1:
     osManang.ren('oldname', 'newname')
     #Examples 2:
     File = osManang.ren('oldname', 'newname')
     print(File)
     ```

8. **`mv(source_path, destination_path)`**
   - **Description:** Moves a file or folder from `source_path` to `destination_path`.
   - **Usage:**
     ```python
     #Examples 1:
     osManang.mv('source_path', 'destination_path')
     #Examples 2:
     File = osManang.mv('source_path', 'destination_path')
     print(File)
     ```

9. **`cd(path)`**
   - **Description:** Changes the current working directory to the specified `path`.
   - **Usage:**
     ```python
     #Examples 1:
     osManang.cd('path')
     #Examples 2:
     path = osManang.cd('path')
     print(path)
     ```

10. **`tree(chomain)`**
    - **Description:** Returns a tree-like structure of the directory at `chomain`.
    - **Usage:**
      ```python
      #Examples 1:
      structure = osManang.tree('path')
      print(structure)
      ```

11. **`pwd()`**
    - **Description:** Returns the current working directory.
    - **Usage:**
      ```python
      #Examples 1:
      cwd = osManang.pwd()
      print(cwd)
      ```

12. **`ls(path)`**
    - **Description:** Lists the contents of the directory at `path`.
    - **Usage:**
      ```python
      #Examples 1:
      contents = osManang.ls('path')
      print(contents)
      ```

13. **`ls_l(path)`**
    - **Description:** Lists the contents of the directory at `path` with details such as size and last modified time.
    - **Usage:**
      ```python
      #Examples 1:
      details = osManang.ls_l('path')
      print(details)
      ```

14. **`istime(path_Name)`**
    - **Description:** Returns the last access time of the specified file.
    - **Usage:**
      ```python
      #Examples 1:
      last_access = osManang.istime('filename.txt')
      print(last_access)
      ```

15. **`size(path_Name)`**
    - **Description:** Returns the size of the specified file.
    - **Usage:**
      ```python
      #Examples 1:
      file_size = osManang.size('filename.txt')
      print(file_size)
      ```

16. **`get_info()`**
    - **Description:** Returns a string containing environment variables and their values.
    - **Usage:**
      ```python
      #Examples 1:
      info = osManang.get_info()
      print(info)
      ```

17. **`get_path()`**
    - **Description:** Returns a string containing executable paths.
    - **Usage:**
      ```python
      #Examples 1:
      exec_paths = osManang.get_path()
      print(exec_paths)
      ```

This module provides a comprehensive set of file and directory management tools suitable for various tasks involving filesystem operations.
