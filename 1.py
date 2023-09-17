#Task 1
a = int(input())
b = int(input())
c=int(input())
print(a + b + c)

#Task 2
b = int(input())
h = int(input())
print(1/2*b*h)

#Task 3
n = int(input())
k = int(input())
print(k//n)
print(k%n)

#Task 4
n=int(input())
hours=n%(60*24)//60
min=n%60
print(hours,min)

#Task 5
name=input()
print("Hello, "+ name + "!")

#Task 6
n=int(input())
x=n+1
y=n-1
print("The next number for the number " + str(n) + " is " +  str(x) + ".")
print("The previous number for the number " + str(n) + " is " +  str(y) + ".")

#Task 7
a=int(input())
b=int(input())
c=int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)

#Task 8
a=int(input())
b=int(input())
l=int(input())
N=int(input())
print(2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)
