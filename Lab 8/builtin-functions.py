#1
from functools import reduce
nums_list = [15,16,17,18]
result = reduce(lambda a, b: a * b, nums_list)
print(f"Answer: {result}")

#2
def char_count(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
           d["upper"]+=1
        elif c.islower():
           d["lower"]+=1
        else:
           pass
    print ("Example: ", s)
    print ("Amount of Upper case characters: ", d["upper"])
    print ("Amount of of Lower case Characters : ", d["lower"])
char_count('IT Management')

#3
def palindrome_words(s):
    string = s.lower().replace(" ", "")
    return string == string[::-1]
example = "Never Odd Or Even" 
if palindrome_words(example):
    print(f"'{example}' is a palindrome.")
else:
    print(f"'{example}' is not a palindrome.")

#4
import time
import math
def square_root(milliscnds, num):
    scnds = milliscnds / 1000
    time.sleep(scnds)
    answer = math.sqrt(num)
    return answer
time_delay = 2123
number = 25100
answer = square_root(time_delay, number)
print(f"{answer}")

#5
def true_tuple(tup):
    return all(tup)
test_tuple = (True, True, True)
result = true_tuple(test_tuple)
print(result)