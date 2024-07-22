# osManag

`osManag`(Operating System Management) is a Python library for managing files and folders easily and quickly. The library includes multiple functions for creating, reading, writing, and deleting files and folders, as well as changing directories and listing directory contents.


## Usage

### Import the Library

```python
import osManag
```

### Available Functions

#### 1. Create a File

```python
osManag.touch('filename.txt')
```

#### 2. Read a File

```python
osManag.cat('filename.txt')
```

#### 3. Write to a File

```python
osManag.nano('filename.txt', 'w', 'Hello, World!')
```

#### 4. Delete a File

```python
osManag.rm('filename.txt')
```

#### 5. Create a Folder

```python
osManag.mkdir('foldername')
```

#### 6. Delete a Folder

```python
osManag.rmdir('foldername')
```

#### 7. Rename a File or Folder

```python
osManag.ren('oldname', 'newname')
```

#### 8. Move a File or Folder

```python
osManag.mv('source_path', 'destination_path')
```

#### 9. Change the Current Directory

```python
osManag.cd('path')
```

#### 10. Display Directory Tree

```python
osManag.tree('path')
```

#### 11. Display Current Directory

```python
osManag.pwd()
```

#### 12. List Directory Contents

```python
osManag.ls('path')
```

#### 13. List Directory Contents with Details

```python
osManag.ls_l('path')
```

#### 14. Display Last Access Time of a File

```python
osManag.istime('filename.txt')
```

#### 15. Display File Size

```python
osManag.size('filename.txt')
```

#### 16. Display System Information

```python
osManag.get_info()
```

#### 17. Display Executable Paths

```python
osManag.get_path()
```

---

These sections provide clear instructions on how to install and use the `osManag` library with examples of each function it offers.

