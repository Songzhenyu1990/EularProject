import os
if __name__ == "__main__":
    for i in range(4,50):
        path = 'p%03d'%i
        if (os.path.exists(path)):
            directory = "./%s/%s.py"% (path, path)
            if(os.path.exists("./%s/%s.py"% (path, path))): continue
            with open(directory, 'w'): pass