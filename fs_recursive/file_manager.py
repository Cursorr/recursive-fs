import os
from .file import File

class FileManager:
    def __init__(self):
        self.files = []

    def fetch(self, path: str, extentions: list=None):
        filesList = []
        fileFilter = True if extentions is not None else False
        if not os.path.exists(path):
            return filesList

        def walk(directory: str):
            try:
                for element in os.listdir(directory):
                    nextFile = directory + "\\" + element
                    if os.path.isfile(nextFile):
                        if fileFilter:
                            if element.split(".").pop() in extentions:
                                filesList.append(File(nextFile))
                        else:
                            filesList.append(File(nextFile))
                    else:
                        walk(nextFile)
            except Exception:
                pass
        
        walk(path)
        self.files = filesList
        return filesList

    def getFileData(self, file: File):
        return {
            "path": file.getPath(),
            "fileName": file.getFilename(),
            "extension": file.getExtention(),
            "size": file.getSize()
        }

    def getAllData(self):
        data = {} 
        for file in self.files:
            data[file.getFilename()] = {
            "path": file.getPath(),
            "extension": file.getExtention(),
            "size": file.getSize()
        }
        return data