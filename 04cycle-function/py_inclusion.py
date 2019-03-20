# list inclusion
mylist = [number for number in range(1, 5) if number % 2 == 0]
print("List created via inclusion:", mylist, end="\n\n")

# dict inclusion
word = "cat"
mydict = { letter: word.count(letter) for letter in word }
print("Dictionary created via inclusion:", mydict, end="\n\n")

# set inclusion
myset = { number for number in range(1, 5) if number % 2 > 0 }
print("Set created via inclusion:", myset, end="\n\n")

print("Tuples do not have inclusions!!")

# generator inclusion
mygen = (number for number in range(1, 5))
print("Generator inclusion type:", type(mygen), end="\n\n")

for number in mygen:
    print("Generator value:", number, end=";\n")

print("Generator is empty now:", list(mygen), end="\n\n")