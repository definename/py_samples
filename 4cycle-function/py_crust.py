a = 1
b = 2
c = 3

e = \
a + \
b + \
c
print("The sum is:", e)

flag = False
collection = []
if collection :
    print("Hey! There are something in collection")
else:
    print("Hey! It's empty")


count = 1
while count <= 5:
    print(count, end='-')
    count += 1
else:
    print("\nThis string will be printed in case if `while` cycle is not interupted by `break`")

# list inclusion
mylist = [number for number in range(1, 5) if number % 2 == 0]
print("List created via inclusion:", mylist)

# dict inclusion
word = "cat"
mydict = { letter: word.count(letter) for letter in word }
print("Dictionary created via inclusion:", mydict)

# set inclusion
myset = { number for number in range(1, 5) if number % 2 > 0 }
print("Set created via inclusion:", myset)

print("Tuples do not have inclusions!!")

# generator inclusion
mygen = (number for number in range(1, 5))
print("Generator inclusion type:", type(mygen))

for number in mygen:
    print("Generator value:", number, end=";\n")

print("Generator is empty now:", list(mygen))