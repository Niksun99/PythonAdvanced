n = 5
ll = []

for _ in range(n):
    ll.append(0)

print(ll)

# creat NxM matrix of zeros
n = 5
m = 3
mm = []
ll = []

for i in range(n):
    ll = []

    for j in range(m):
        ll.append(i * n + j)
    mm.append(ll)

print(mm)
# chomprehnsion

ll = [1, 2, 3, 4, 5, 6, 7]
ll2 = []
for v in ll:
    ll2.append(v + 1)
print(ll)
print(ll2)

ll3 = [v + 1 for v in ll]
print(ll3)

mm = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8],
    [10, 11, 12],

]

print(mm)
print(
    [[v + 1 for v in row] for row in mm]
)
