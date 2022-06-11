row_count, columns_count = [int(x) for x in input().split(', ')]
matrix = []
print(row_count)
print(columns_count)

for _ in range(row_count):
    matrix.append(
        [int(x) for x in input().split(', ')]
    )

print(matrix)

column_sums = [0] * columns_count

for row_index in range(row_count):
    for column_index in range(columns_count):
        column_sums[column_index] += matrix[row_index][column_index]

[print(x) for x in column_sums]
