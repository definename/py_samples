import math

msg = 61
print(msg)

print(type(123))

print(divmod(9,5))

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

poem ='''111
222'''
print(poem)

# strings
print(str(True))

start = "Na-" *4
print(start)
print(start[0], start[1], start[-1],sep='')

stop = start.replace("-", "+", 2)
print(stop)
print(start)

letters = '0123456789'
print(letters[:])
print(letters[2:])
print(letters[2:5])
print(letters[-1:])
print(letters[::2])
print(letters[-1::-1])

print("Len is:", len(letters))

verbs = "get, got, gotten"
print(verbs.split(","))

verbStr = "; ".join(verbs.split(","))
print(verbStr)