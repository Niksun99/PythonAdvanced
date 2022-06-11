try:
    # Not existing file
    open('./demo.py')
except FileNotFoundError:
    print('File is not found')