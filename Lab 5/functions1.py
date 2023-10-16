#1
def grams_ounces(x):
    ounces=28.3495231 * grams
    return ounces
    
grams=1000
ounces=grams_ounces(grams)
print (ounces)


#2
def fah_cen(F):
    centigrade=(5/9)*(F-32)
    return centigrade
    
F=float(input())
centigrade=fah_cen(F)
print(centigrade)

#3
def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    if x<0 or y<0 or x!=int(x) or y!=int(y):
        return "Not found"
    return int(x), int(y)
numheads = 35
numlegs = 94
answer = solve(numheads, numlegs)
print(answer)


#4
def prime_nums(n):
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

def filter_prime(numbers):
    prime_numbers = [n for n in numbers if prime_nums(n)]
    return prime_numbers

#5
from itertools import permutations
def print_permutations(input_string):
    p_list = permutations(input_string)
    for p in p_list:
        print(''.join(p))
user_input=input()
print_permutations(user_input)

#6
def reverse_sent(sent):
    n = sent.split()
    reversed_n = ' '.join(reversed(n))
    return reversed_n
user_input = input()
reversed_n = reverse_sent(user_input)
print(reversed_n)

#7
def has_33(n):
    for i in range(len(n) - 1):
        if n[i] == 3 and n[i + 1] == 3:
            return True
            return False
print(has_33([int(s) for s in input().split()]))   

#8
def spy_game(nums):
    count_1 = 0
    count_2 = 0
    for n in nums:
        if n==0 and count_2==0:
            count_1 += 1
        elif n==0 and count_2==1:
            count_1 += 1
        elif n==7 and count_1==2:
            count_2 += 1
    return count_1==2 and count_2==1
print(spy_game([int(s) for s in input().split()])) 

#9
def vol_of_sph(rad):
    vol= (4/3)*3.14*(rad^3)
    return vol
rad = int(input())
vol = vol_of_sph(rad)
print(f"{vol:.2f}")

#10
def unique_elements(n):
    unique_list = []
    for element in n:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
print(unique_elements([int(s) for s in input().split()]))  
       

#11

def check(str) :
    if str[  -1 : - len(str) - 1  : -  1] == str:
        print ("Palindrome")
    else :
        print ("Not a palindrome ")

string = str(input())
check(string)

#12
def histogram(nums):
        for n in range(0,len(nums)):
                print('*' * list[n])
        return
list=[int(n) for n in input().split()]
histogram(list)

#13
import random
def guess():
    rand_number = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    count = 0
    while True:
        print("Take a guess.")
        guess_num = int(input())
        count += 1
        if guess_num < rand_number:
            print("Your guess is too low.")
        elif guess_num > rand_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break
guess()