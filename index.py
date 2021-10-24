from fs_recursive.file_manager import FileManager
import os

directory = os.getcwd()
extentions = ["py", "json"]

filemanager = FileManager()

files = filemanager.fetch(directory, extentions)

print(filemanager.getAllData())