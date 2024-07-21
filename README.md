### Man_os2
### Library Name: `Man_os2`

#### Role:
The `Man_os2` library provides a set of utility functions for file and directory management tasks such as creating, removing, renaming, and listing files and directories. It also includes functions for file operations like reading and writing, as well as retrieving system and environmental information.



#### Functions and Usage:

1. **`touch(File_Name)`**: Creates an empty file if it doesn't already exist.

   ```python
   import Man_os2

   print(Man_os2.touch("example.txt"))
   ```

2. **`cat(File_Name)`**: Reads the content of a file.

   ```python
   print(Man_os2.cat("example.txt"))
   ```

3. **`nano(File_Name, Mode, Write)`**: Writes content to a file. The mode can be 'w' (write) or 'a' (append).

   ```python
   print(Man_os2.nano("example.txt", "w", "Hello, world!"))
   ```

4. **`rm(File_Name)`**: Removes a file.

   ```python
   print(Man_os2.rm("example.txt"))
   ```

5. **`mkdir(Folder_Name)`**: Creates a new directory.

   ```python
   print(Man_os2.mkdir("new_folder"))
   ```

6. **`rmdir(Folder_Name)`**: Removes a directory.

   ```python
   print(Man_os2.rmdir("new_folder"))
   ```

7. **`ren(Name, New_Name)`**: Renames a file or directory.

   ```python
   print(Man_os2.ren("old_name.txt", "new_name.txt"))
   ```

8. **`mv(source_path, destination_path)`**: Moves a file or directory from one path to another.

   ```python
   print(Man_os2.mv("file.txt", "new_location/file.txt"))
   ```

9. **`cd(path)`**: Changes the current working directory.

   ```python
   print(Man_os2.cd("/path/to/directory"))
   ```

10. **`tree(chomain)`**: Lists all files and directories in a directory tree.

    ```python
    print(Man_os2.tree("."))
    ```

11. **`pwd()`**: Returns the current working directory.

    ```python
    print(Man_os2.pwd())
    ```

12. **`ls(path)`**: Lists files and directories in a specified path.

    ```python
    print(Man_os2.ls("."))
    ```

13. **`ls_l(path)`**: Lists files and directories with detailed information such as size and last modified time.

    ```python
    print(Man_os2.ls_l("."))
    ```

14. **`istime(path_Name)`**: Returns the last access time of a file.

    ```python
    print(Man_os2.istime("example.txt"))
    ```

15. **`size(path_Name)`**: Returns the size of a file.

    ```python
    print(Man_os2.size("example.txt"))
    ```

16. **`get_info()`**: Retrieves and returns system environmental variables.

    ```python
    print(Man_os2.get_info())
    ```

17. **`get_path()`**: Retrieves and returns executable paths.

    ```python
    print(Man_os2.get_path())
    ```



