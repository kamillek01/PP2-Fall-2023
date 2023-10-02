#Task 2
s=input()
A=[int(s) for s in s.split()]
for i in A:
    if int(i)%2 == 0:
       print(i, end=' ')