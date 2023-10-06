y, z = [int(x) for x in input().split()]
b = set()
for i in range(z):
    a_i, b_i = [int(x) for x in input().split()]
    for j in range(a_i, y + 1, b_i):
        b.add(j)
c = set()
for i in range(6, y + 1, 7):
    c.add(i)
for i in range(7, y + 1, 7):
    c.add(i)
b -= c
print(len(b))