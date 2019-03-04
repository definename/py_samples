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

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
for rabbit in rabbits:
    print(rabbit, end=";\n")

word = "cat"
for letter in word:
    print(letter, end=";\n")
    break
else:
    print("This string will be printed in case if `for` cycle is not interupted by `break`")

list1 = [1, 2, 3, 4]
list2 = ["1", "2", "3"]
for first, second in zip(list1, list2):
    print(first, "+", second, "=", first + int(second))

for val in range(1, 4, 2):
    print("range value:", val)

# list inclusion
mylist = [number for number in range(1, 5) if number % 2 == 0]
print("List created via inclusion:", mylist)

# dict inclusion
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