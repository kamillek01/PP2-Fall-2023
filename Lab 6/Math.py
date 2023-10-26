#1
import math
dgrs = float(input())
rdn = math.radians(dgrs)
print(f"{rdn} radians")

#2
import math
height = float(input("Height: "))
first_base = float(input('Base, first value: '))
second_base = float(input('Base, second value: '))
Area = ((first_base + second_base ) / 2) * height
print("Area:", Area)

#3
from math import tan, pi
sds = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
area = sds * (length ** 2) / (4 * tan(pi / sds))
print("The area of the polygon is: ",area)

#4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
Area = base * height
print(f"Output: {Area}")