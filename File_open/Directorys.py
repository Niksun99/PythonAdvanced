from os import mkdir, rmdir, listdir
import time
from os.path import join,abspath

directory_path = './'
# mkdir('./dir_to_delete') suzdava directory
# rmdir('./dir_to_delete') iztriva


files_and_dirs_names = listdir(directory_path)
files_and_dirs = [
    join(directory_path, f) for f in files_and_dirs_names
]

[print(f) for f in files_and_dirs_names]
[print(f) for f in files_and_dirs]