from pathlib import Path
import os
from humanize import naturalsize

def get_siz(path='.'):
    size = 0
    for fil in Path(path).rglob('*'):
        size += fil.stat().st_size
       
        
    return naturalsize(size)

if __name__=='__main__':
    di = os.listdir()
    path = "D:/"
    for path, directory, files in os.walk(path):
        #print(path)
        print("File {} {}".format(path, get_siz(path)))
