from filelist import filelist
import os

files = filelist(os.getcwd(), False)

print(files)