#Task 12
n=int(input())
m=int(input())
k=int(input())
if m*n>k and ((k%m==0) or (k%n==0)):
    print("YES")
else:
    print("NO")
