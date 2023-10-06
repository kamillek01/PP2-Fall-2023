def print_set(some_set):
    print(len(some_set))
    print(*[str(item) 
    for item in sorted(some_set)])

X, Y = [int(s) for s in input().split()]
colors1, colors2 = set(), set()
for i in range(X):
    colors1.add(int(input()))
for i in range(Y):
    colors2.add(int(input()))
    
print_set(colors1 & colors2)
print_set(colors1 - colors2)
print_set(colors2 - colors1)