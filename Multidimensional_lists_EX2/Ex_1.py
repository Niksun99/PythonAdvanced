sublist = input().split('|')

result = []

for idx in range(len(sublist) - 1, -1, -1):
    current_el = sublist[idx].strip().split()
    result.extend(current_el)

print(' '.join(result))
