file = open('demos.txt', 'r')

while True:
    line = file.readline()
    if not line:
        break
    print(line)

print('-' * 20)
file = open('demos.txt', 'r')

print(file.readlines(2))

print('-'*20)

file = open('demos.txt', 'r')
print(file.readlines())
print('-'*20)

file = open('demos.txt', 'r')
print("---looops----")
for line in file:
    print(line)
file = open('demos.txt', 'r')
print('---chomprehension---')
print([
    line.strip() for line in file
])

