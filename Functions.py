# Type hinting:
def add(a : float, b : float):
    return a + b


print(add(5,5))
print(add(55,51))
print(add(-3,2))
print(add(-60,0))


def max(x,y):
    """
    Args:
        x, y: int or float
    """
    if x > y: return x
    else: return y


print(max(0,1))
print(max(1,1))
print(max(2,1))
print(max(21,1))


def f(x):
    """
    Args:
        x int or float
    """
    y = 1
    x += y
    print('x = ' + str(x))
    return x


print(f(2))
print(f(22))
print(f(-2))



x = 3
y = 2
z = f(x)
print('z = ' + str(z))
print('x = ' + str(x))
print('y = ' + str(y))


def square(x): return x*x


print(square(5))
print(square(7))
print(square(0))
print(square(1))


def get_students():
    students = ["mate", "jure"]

    def get_students_titlecase():
        students_titlecase = []
        for s in students: students_titlecase.append(s.title())
        return students_titlecase
    print(get_students_titlecase())

get_students()


def two_power(x, n):
    while n > 1:
        x = square(x)
        n /=2
    return x


print(two_power(2,5))
print(two_power(2,4))
print(two_power(5,3))
print(two_power(3,3))


def find_root1(x, power, epsilon):
    low = 0
    high = x
    ans = (low + high) / 2
    while(abs(ans**power-x)) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2
    return ans


print(find_root1(25, 2, 0.001))
print(find_root1(27, 3, 0.001))
print(find_root1(-27, 3, 0.001))


def find_root2(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None # can't find even powered root of negative numbers
    low = min(0,x)
    high = max(0,x)
    ans = (high + low) / 2
    while(abs(ans**power-x) > epsilon):
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans


print(find_root2(25, 2, 0.001))
print(find_root2(27, 3, 0.001))
print(find_root2(-27, 3, 0.001))
print(find_root2(0.25, 2, 0.001))


def find_root3(x, power, epsilon):
    """
    x and epsilon int or float, power an int
    epsilon > 0 & power >= 1
    returns a float y s.t. y ** power is within epsilon of x.
    If such a float does not exist, it returns None
    """
    if x < 0 and power % 2 == 0:
        return None # can't find even powered root of negative numbers
    low = min(-1,x)
    high= max(1,x)
    ans = (low+high)/2
    while(abs(ans**power-x) >epsilon):
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (low+high)/2
    return ans


print(find_root3(25, 2, 0.001))
print(find_root3(27, 3, 0.001))
print(find_root3(-27, 3, 0.001))
print(find_root3(0.25, 2, 0.001))


import circle
pi = 3
print(pi)
print(circle.pi)
print(circle.area(3))
print(circle.circumference(3))


from circle import *
pi = 0


print(pi)
print(area(3))
print(circumference(3))


def a(x, y, z):
    if x:
        return y
    else:
        return z


a(True, 2, 1)
a(False, 2, 1)

def b(q, r):
    return a(q>r, q, r)


print(b(a, b))
print(a(3>2, a, b))


def iterative_power(x, p):
    x = float(input('Enter a number: '))
    p = int(input('Enter an integer power: '))
    result = 1
    for turn in range(p):
        print('iteration: ' + str(turn) + 'current result: ' + str(result))
        result *= x


print(iterative_power(5,3))
print(iterative_power(2,6))


def eval_quadratic(a, b, c, x): return a * x**2 + b * x + c


print(eval_quadratic(5,3,2,9))
print(eval_quadratic(6,7,2,13))


def clip(lo, x, hi):
    """
    lo < hi
    return lo if x < lo
    return hi if x > hi
    """
    return min(hi,max(x, lo))


print(clip(5,3,0))
print(clip(12,35,20))
print(clip(4,25,99))


x = 12
def g(x):
    x += 1
    def h(y):
        return x + y
    return h(6)


print(g(x))


def foo(x):
    def bar(x):
        return x + 1
    return bar(x * 2)


print(foo(3))


def foo(x):
    def bar(z):
        return z + x
    return bar(3)


print(foo(2))


def fourth_power(x): return square(square(x))


print(fourth_power(4))
print(fourth_power(2))
print(fourth_power(5))


def odd(x): return x % 2 == 1

print(odd(52))
print(odd(2))
print(odd(0))
print(odd(12))
print(odd(7))

def is_vowel(char):
    char = char.lower()
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

print(is_vowel("z"))
print(is_vowel("e"))
print(is_vowel("m"))
print(is_vowel("h"))
print(is_vowel("a"))

def is_vowel2(char):
    char = char.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    return char in vowels


print(is_vowel2("z"))
print(is_vowel2("e"))
print(is_vowel2("m"))
print(is_vowel2("h"))
print(is_vowel2("a"))


# Lambda functions:
def double(x): return x * x


lambda_double = lambda x: x * x


print(lambda_double(5))
print(lambda_double(7))

add = lambda a, b: a + b

print(add(5,2))
print(add(5,5))


# Variable number of arguments:
def var_args(name ,*args):
    print(name)
    print(args)

var_args("Python", "is cool")
var_args("Python", "is", "cool")
var_args("Something", range(5))


# Keyword arguments
def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])

var_args("Python", description = "...", feedback = None)
var_args("Python", description = "...", feedback = ",,,")


# Generator Functions - Yield
def create_generator():
    yield 1
    yield 2

my_gen = create_generator()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
