# -*- coding: utf-8 -*-
num = 5
if num == 5: print(num)
if num: print(num)


num = 0
if num == 0: print(num)
if num: print(num)


num = -1
if num == -1: print(num)
if num: print(num)


text = "Python"
if text: print(text)

text = ""
if text: print(text)


python_course = True
if python_course: print("This will execute")


aliens_found = False
if aliens_found: print("This will NOT execute")

l = []
if l: print(l)

l1 = [1,2,3]
if l1: print(l1)


# NOT IF:
num = 5
if num != 5: print("This will not execute")


python_course = True
if not python_course: print("This will also not execute")


# MULTIPLE IF:
num = 5
python_course = True


if num and python_course:
    print("this will execute")


if num or python_course:
    print("this will also execute")


if num:
    if python_course:
        print("this will execute")


# Ternary If Statements
a = 20
b = 50
print("bigger" if a > b else "smaller")

h = 32
if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else:
    print("Between 20 and 50")
    

h = 32
if h > 50:
    print("Greater than 50")
else:
    if h < 20:
        print("Less than 20")
    else:
        print("Between 20 and 50")