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