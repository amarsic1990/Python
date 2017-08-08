# -*- coding: utf-8 -*-
x = 500
y = 500

print(id(x))
print(id(y))

x = 1000
print(id(x))


print(__name__)

l = [2,4,6]
l1 = [2,4,6]

print(l == l1)
print(l is l1)

l2 = [2,4,6]
l3 = l2
print(l2 == l3)
print(l2 is l3)

