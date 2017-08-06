# square
x = 3
ans = 0
iterLeft = x

while(iterLeft != 0):
    ans += x
    iterLeft -= 1
print(str(x) + ' * ' + str(x) + ' = ' + str(ans))



# Cube root
x = int(input('Enter an integer: '))
ans = 0


while (ans ** 3 < abs(x)):
    ans += 1
if ans ** 3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))


x = int(input('Enter an integer: '))

for ans in range(0, abs(x)+1):
    if ans ** 3 == abs(x):
        break
if ans ** 3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = - ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))


# range
for i in range(20): print(i)
for i in range(0,20): print(i)
for i in range(1,20): print(i)
for i in range(0,20,2): print(i)


num = 256
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = int(num / 2)
if isNeg:
    result = '-' + result
print(result)


# decimal to binary fraction
x = float(raw_input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))


x = 23
epsilon = 0.01
step = epsilon ** 2
numGuesses = 0
ans = 0
while(abs(ans**2-x) >= epsilon and ans <= x):
    ans += step
    numGuesses += 1
print('numGuesses = ' + str(numGuesses))
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + 'is close to square root of ' + str(x))


x = 25
epsilon = 0.01
step = 0.1
guess = 0.0
while abs(guess**2 - x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break
if abs(guess ** 2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))


# sqrt bisection
x = 25
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (high + low) / 2

while(abs(ans**2-x) >= epsilon):
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans ** 2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low)/2
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))


x =  0
while(x < 10):
    x += 2
    print(x)
print("Goodbye!")

myStr = '6.00x'
for char in myStr:
    print(char)
print('done')


greeting = 'Hello!'
count = 0
for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in school:
    if char in vowels:
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1
print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))


divisior = 2
for num in range(0,10,2): print(num/divisior)


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo')


for i in range(2,11,2): print(i)
print('Goodbye')


print('Hello!')
for i in range(10,1,-2): print(i)


xy = 6
ans = 0
for i in range(xy+1): ans += i
print(ans)


iteration = 0
count = 0
while iteration < 5:
    for letter in 'hello, world':
        count += 1
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
    iteration += 1


iteration = 0
while iteration < 5:
    count = 0
    for letter in 'hello, world':
        count += 1
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
    iteration += 1


iteration = 0
while iteration < 5:
    count = 0
    for letter in 'hello, world':
        count += 1
        if iteration % 2 == 0:
            break
    print('Iteration ' + str(iteration) + '; count is ' + str(count))
    iteration += 1


count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))



print('Please think of a number between 0 and 100!')
lb = 0
hb = 100
ans = int((hb + lb) / 2)
while True:
    print('Is your secret number ' + str(ans) + '?')
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
    if a == 'h':
        hb = ans
    elif a == 'l':
        lb = ans
    elif a == 'c':
        print('Game over. Your secret number was: '+str(ans))
        break
    else:
        print('Sorry, I did not understand your input.')
        continue
    ans = int((hb+lb)/2)


# Newton-Raphson
epsilon = 0.01
y = 24
guess = y/2.0
while(abs(guess*guess-y) >= epsilon):
    guess = guess -(((guess**2)-y)/(2*guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))
