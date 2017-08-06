# -*- coding: utf-8 -*-
print(type(3))
print(type(3.0))
print(float(3))
print(int(3.9))


print(3*'a')
print('a'+'a')
print('a'+str(3))
print(len('abc'))


print('abc'[0])
print('abc'[2])
#print('abc'[3]) IndexError
print('abc'[-1])
print('abc'[1:3])


name = input('Enter your name: ')
print('Are you ' + name + '?')


x = int(input('Enter an integer: '))
if x % 2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')


x = int(input('Enter an integer: '))
if x % 2 == 0:
    if x % 3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x % 3 == 0:
    print('Divisible by 3 and not by 2')


print(type(None))


print(round(2.6))
print(int(2.6))

s = 'Python is Fun!'
print(s[1:12:2])
print(s[::2])
print(s[1:12:3])

str1 = 'hello'
str2 = ','
str3 = 'world'
print(str1[0])
print(str1[-1])
print(len(str1))
print(str1+str2+str3)
print(3*str3)
print('hello'==str1)
print('a' in str1)
str4 = str1 + str3
print(str4)
print('low' in str4)
print(str3[1:3])
print(str3[:3])
print(str3[:-1])
print(str1[1:])
print(str4[1:9])
print(str4[1:9:2])

print(str4[::-1])


varA = 22
varB = 21
if type(varA) == str or type(varB) == str: print('string involved')
elif varA > varB: print('bigger')
elif varA == varB: print('equal')
elif varA < varB: print('smaller')
