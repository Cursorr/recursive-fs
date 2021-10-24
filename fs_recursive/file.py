import os 

class File:
    def __init__(self, path: str):
        self.path = path
        self.file = self.path.split("\\").pop()
        self.size = os.path.getsize(path)
        self.access = lambda mode: os.access(self.path, mode)
    
    def getPath(self):
        return self.path

    def getFile(self):
        return self.file
        
    def getFilename(self):
        return self.file.split(".")[0]

    def getExtention(self):
        return self.file.split(".").pop()

    def getSize(self):
        return self.size

    def getStats(self):
        stats = ["mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"]
        result = os.stat(self.path)
        return {stats[result.index(stat)]: stat for stat in result}

    def canRead(self):
        return self.access(os.R_OK)

    def canWrite(self):
        return self.access(os.W_OK)
        
    def canExecute(self):
        return self.access(os.X_OK)