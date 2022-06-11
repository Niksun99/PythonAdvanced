file_path = './demos.txt'
print('----whole file---')

file = open(file_path, 'r')
print(file.read())

print('-----Bites----')
# chete tolkova simwoli kolkoto se dali v skobite i pomni do kude e


file = open(file_path, 'r')
while True:
    chars = file.read(1)
    if not chars:
        break
    print(chars)