#1
import os
path = r'C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Лабки оптимизация'
print("List only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nList only files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nList all directories and files :")
print([ name for name in os.listdir(path)])

#2
import os
print('Exist:', os.access(r'C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Лабки оптимизация', os.F_OK))
print('Readable:', os.access(r'C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Лабки оптимизация', os.R_OK))
print('Writable:', os.access(r'C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Лабки оптимизация', os.W_OK))
print('Executable:', os.access(r'C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Лабки оптимизация', os.X_OK))


#3
import os
def exist_check(path):
   if os.path.exists(path):
       filen = os.path.basename(path)
       dir = os.path.dirname(path)
       print(f"Filename: {filen}")
       print(f"Directory: {dir}")
    else:
       print(f"The path '{path}' does not exist.")
path = r'C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Лабки оптимизация'
exist_check(path)

#4
with open(r'C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Лабки оптимизация\Test.txt', 'r') as file:
    cnt = 0
    for line in file:
        if line != "\n":
            cnt += 1
print(cnt)

#5
def add_list(path, input_list):
    try:
        with open(path, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"The given list added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
path = r'C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Лабки оптимизация\Test.txt'
example = ['Principles of programming']
add_list(path, example)

#6
import string 
import os
if not os.path.exists("letter"):
   os.makedirs("letter")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#7
from shutil import copyfile
copyfile('first.txt', 'second.txt')


#8
import os
if os.path.exists("second.txt"):
  os.remove("second.txt")
  print("Deleted")
else:
  print("Does not exist!")









