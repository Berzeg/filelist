from filelist import filelist
import os

path = os.path.join(os.getcwd(), 'example')
files = filelist(path, False, ".pyignore")

print(files)