from io import open


# import io

def print_contents(file_path):
    print(f'---- Openning {file_path} ---')
    file = open('demos.txt')
    print(file.read())


# Relative

print_contents('demos.txt')
print_contents('./Test.py')
print_contents('../Eror_Handling/Ex_1.py')
