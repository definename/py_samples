import gc
import sys
import math

msg = 61
print(msg)

print(type(123))

print(divmod(9, 5))

print(0b10, 0o10, 0x10, sep=",")

b = int("123") + 1
print(b)

print(True + 1)

googol = 10**100
print(googol)

print(float("1.1"))

# math library

print(math.pi)
print(math.pow(8, 2))
print("'Snap'")

poem = '''111
222'''
print(poem)

# strings
print(str(True))

start = "Na-" * 4
print(start)
print(start[0], start[1], start[-1], sep='')

stop = start.replace("-", "+", 2)
print(stop)
print(start)

print()

letters = '0123456789'
print("origin: {}".format(letters))
print("[:] {}".format(letters[:]))
print("[2:] {}".format(letters[2:]))
print("[2:5] {}".format(letters[2:5]))
print("[-1:] {}".format(letters[-1:]))
print("[::2] {}".format(letters[::2]))
print("[-1::-1] {}".format(letters[-1::-1]))
print("[0:2] {}".format(letters[1:3]))
print("[9:10] {}".format(letters[9:10]))

print()

print("Here is lenght of the string:", len(letters))

verbs = "get, got, gotten"
print("Here is result list:", verbs.split(","))

verbStr = "; ".join(verbs.split(","))
print("Here is list joined into the string:", verbStr)

a = 1
b = 1
print(a is b)

a = 100000
b = 100000
print(a is b)

print("Reference count for 'a': {}".format(sys.getrefcount(a)))

print("Garbage collector has just destroyed: {} objects".format(gc.collect()))

print(1 < 3 < 5 > 99)

if 0.1 + 0.2 == 0.3:
    print("Equal")
else:
    print("Not equal")

print(r"c:\new\files\rawstring.py")

print("ab" not in "abc")
print(not "ab" in "abc")

num1 = 5
num2 = 2

print("{}".format(num1 / num2))
print("{}".format(num1 // num2))


a = 1
b = 2
if a == 1 and b == 2:
    print("123")
