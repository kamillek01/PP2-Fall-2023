#1
def squares_of_nums(n):
    for i in range(1, n + 1):
        yield i**2

n = int(input()) 
squares_gen = squares_of_nums(n)

for square in squares_gen:
    print(square)

#2
def even_nums(n):
    for num in range(0, n + 1, 2):
        yield num

n = int(input())
even_numbers = even_nums(n)
even_numbers_list = list(even_numbers)  
comma_separated = ", ".join(map(str, even_numbers_list))
print( {comma_separated})

#3
def div_by_3_4(n):
    for num in range(0, n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input())
for number in div_by_3_4(n):
    print(number)

#4
def squares_generators(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input())
b = int(input())

for square in squares_generators(a, b):
    print(square)

#5
def count_down_from_(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
print(f"Countdown from {n} to 0:")
for num in count_down_from_(n):
    print(num)