import math
#1
class Input_Upper( object):
    def __init__(self):
        self.str=" "
    def getString(self):
        self.str=input()
        
    def printString(self):
        print(self.str.upper())
            
str_Object=Input_Upper()
str_Object.getString()
str_Object.printString()

#2
class Shape:
    def __init__(self):
        pass
    def Area(self):
        return 0
      
class Square(Shape):
    def __init__(self, l):
        self.length = l

    def Area(self):
        self.area = self.length*self.length
        return self.area

shape = Shape()
print(shape.Area())

length = float(input())
square = Square(length)
print(square.Area())

#3
class Shape:
    def Area(self):
        return 0
   

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Area(self):
        self.area = self.length*self.width
        return self.area
    
length = float(input())
width = float(input())
rectangle = Rectangle(length, width)
print(rectangle.Area())


#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self,x2, y2):
        self.x = x2
        self.y = y2

    def dist(self, point2):
        dx = self.x-point2.x
        dy = self.y-point2.y
        dis = math.sqrt(dx**2 + dy**2)
        return dis
    
pnt1=int(input())
coord1=int(input())

pnt2=int(input())
coord2=int(input())

point1 = Point(pnt1, coord1)
point2 = Point(pnt2, coord2)

point1.show()

pnt3=int(input())
coord3=int(input())

point1.move(pnt3, coord3)
point1.show()

distance = point1.dist(point2)
print(distance)

#5

class bank_Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, plus):
        self.depos = self.balance + plus
        print(self.depos)

    def withdraw(self, minus):
        if(self.balance>=minus):
            self.withdrawal = self.balance - minus
            print(self.withdrawal)
        else:
            print('Insufficient balance. There is no availability to withdraw.')

owner_name = input()
balance_card = float(input())
account = bank_Account(owner_name, balance_card)

print(f"{owner_name}, you have {balance_card} on your balance card, please, press 1 if you want to deposit or Press 0 if you want to withdraw")
x = int(input())
if(x==1):
    add = float(input())
    account.deposit(add)
elif(choice==0):
    substract = float(input())
    account.withdraw(substract) 

    #6
def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

prime_num = list(filter(lambda x: prime(x), num))

print("Prime numbers:", prime_num)

