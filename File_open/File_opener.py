file_path = 'demos.txt'
try:
    open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('file not found')
