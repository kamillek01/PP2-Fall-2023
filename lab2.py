#Task 1
a=int(input())
b=int(input())
if a>b:
    print(b)
else:
    print(a)


#Task 2
x=int(input())
if x>0:
    print(1)
elif x<0:
    print(-1)
else:
    print(0)


#Task 3
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if (x+y+a+b) % 2 ==0:
    print("YES")
else:
    print("NO")

#Task 4
a=int(input())
if (a%4==0 and a%100!=0) or (a%400==0):
    print("YES")
else:
    print("NO")

#Task 5
a=int(input())
b=int(input())
c=int(input())
if a<=b and a<=c:
    print(a)
elif b<=a and b<=c:
    print(b)
else:
    print(c)

#Task 6
a=int(input())
b=int(input())
c=int(input())
if a==b and a==c:
    print(3)
elif (a==b) or (a==c) or (b==c):
    print(2)
else:
    print(0)

#Task 7
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if(x==a or y==b):
    print("YES")
else:
    print("NO")

#Task 8
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if abs(x-a) <=1 and  abs(y-b) <=1:
    print("YES")
else:
    print("NO")

#Task 9
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if abs(x-a)== abs(y-b):
    print("YES")
else:
    print("NO")

#Task 10
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if abs(x-a)==abs(y-b) or x==a or y==b:
    print("YES")
else:
    print("NO")

#Task 11
x=int(input())
y=int(input())
a=int(input())
b=int(input())
x1 = abs(x - a)
y1 = abs(y - b) 
if x1 == 1 and y1 == 2 or x1 == 2 and y1 == 1:
    print("YES") 
else:
    print("NO")

#Task 12
n=int(input())
m=int(input())
k=int(input())
if m*n>k and ((k%m==0) or (k%n==0)):
    print("YES")
else:
    print("NO")

#Task 13
N=int(input())
M=int(input())
x=int(input())
y=int(input())
if N > M:
    N, M = M, N
if x >= N / 2:
    x = N - x
if y >= M / 2:
    y = M - y
    
if x < y:
    print(x)
else:
    print(y)