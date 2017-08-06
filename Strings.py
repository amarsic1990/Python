# -*- coding: utf-8 -*-
import webbrowser

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

# escape sequence
escape_seq = "https://www.quackit.com/python/reference/python_3_escape_sequences.cfm"
webbrowser.open(escape_seq)

print("anti\'c")
print("anti\\c")


# encode/decode
name = "mark"
print(name)
name_byte = name.encode("utf-8")
print(name_byte)
name_decode = name_byte.decode("utf-8")
print(name_decode)