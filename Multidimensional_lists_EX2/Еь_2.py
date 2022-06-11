size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == 'END':
        break
    parts = line.split(' ')
    command = parts[0]
    row, cow, value = [int(x) for x in parts[1:]]

    if row < 0 or cow < 0 or row >= size or cow >= size:
        print('Invalid coordinates')
        continue

    if command == 'Add':
        matrix[row][cow] += value
    else:
        matrix[row][cow] -= value
for row in matrix:
    print(*row, sep=' ')
