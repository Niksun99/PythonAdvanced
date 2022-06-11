file_path = './demos.txt'

file1 = open(file_path, 'w')
file2 = open(file_path, 'w')

file1.write('file 11')
file1.close()
file2.close()
file2.write('file 2')
