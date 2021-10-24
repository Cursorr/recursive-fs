# Recursive-fs

Easily access your files in any folder or sub-folder.

## Objective

It is often difficult to retrieve and use files stored locally at your application, `fs-recursive` allows you to retrieve any file saved in a folder or sub-folder at a defined location.

## How to use

The `fs-recursive` is very simple to use, you need to use the followed function :

```py
fetch(
  directory: string,
  extentions: list or None
) -> list

getFileData(
  file: File
 ) -> dict

getAllData () -> dict
```

### An example is always more telling

```py
from fs_recursive.file_manager import FileManager
import os

directory = os.getcwd()
extentions = ["py", "json"]

filemanager = FileManager()

files = filemanager.fetch(directory, extentions)  #return the list of retrived files Objects (fs_recursive.File) 

print(filemanager.getFileData(files[0]))

/**
 * Log the followed result
 *
 * {
 *    'path': 'E:\\WindowsData\\Desktop\\recursive-fs\\fs_recursive\\file.py',
 *    'fileName': 'file',
 *    'extension': 'py',
 *    'size': 1098  👈 expredded in bytes
 * }
 */
```

Then you can access to other data like this

```py
files = filemanager.fetch(directory, extentions)

print(files[0].getStats())

/**
 * {
 *    'mode': 33206,
 *    'ino': 7881299347949034,
 *    'dev': 4131345398,
 *    'nlink': 1,
 *    'uid': 0,
 *    'size': 1098,
 *    'atime': 1635076111,
 *    'mtime': 1635075571,
 *    'ctime': 1635018989
 * }
 *
 */
```

You can sort results by their extension

```py
from fs_recursive.file_manager import FileManager

directory = os.getcwd()
extentions = ["py", "json"]

files = filemanager.fetch(directory, extentions)


print(filemanager.getAllData());

/**
 * Log the followed result
 *
 * {
 *   'file_manager': {
 *       'path': 'E:\\WindowsData\\Desktop\\recursive-fs\\fs_recursive\\file_manager.py',
 *       'extension': 'py',
 *       'size': 1529
 *    },
 *    'data': {
 *       'path': 'E:\\WindowsData\\Desktop\\recursive-fs\\data.json',
 *       'extension': 'json',
 *       'size': 234
 *     }
 * }
 */
```

# Credits

Recursive-fs was done in TypeScript by LeadCodeDev `github.com/LeadcodeDev/recursive-fs` and i just reporoduced it in Python. Thanks for him for letting me do it and get his ReadME file base.
