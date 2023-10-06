a, b = set(), set()
for i in range(int(input())):
    s = set()
    for j in range(int(input())):
        s.add(str(input()))
    if i == 0:
        a = s
    else:
        a &= s
    b |= s    
b = sorted(b)
a = sorted(a)
print(len(a))
for i in a:
    print(i)
print(len(b))
for i in b:
    print(i)