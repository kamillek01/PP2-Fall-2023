list=input().split()
x=set()
for num in list:
    if num in x:
        print("YES")
    else:
        print("NO")
        x.add(num)