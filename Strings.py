print('Hello World')
print("Hello World")
print("""Hello World""")


print("Hello World".capitalize())
print("Hello World".replace("e", "a"))
print("Hello".isalpha())
print("123".isdigit()) # useful when converting str to int


print("first, second, third".split(","))


# String Format Function:
name = "John"
surname = "Doe"
print("Nice to meet you {0} {1}".format(name, surname))
print("Nice to meet you {} {}".format(name, surname))

# String Interpolation:
name = "John"
surname = "Doe"
print(f"Nice to meet you {name} {surname}")
