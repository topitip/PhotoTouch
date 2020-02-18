import os
import uuid


class FileStorage:

    def __init__(self, dir):

        self.dir = dir
        if not os.path.exists(dir):
            os.mkdir(dir)
    
    def load(self, param):

        obj = b''.join(param.file.readlines())

        ext = param.filename.split('.')[-1:][0]

        file_path = self.dir + '/' + uuid.uuid4().hex + '.' + str(ext)

        with open(file_path, "wb") as f:
            f.write(obj)
            f.close()
        
        return file_path


filestorage = FileStorage('storage')
