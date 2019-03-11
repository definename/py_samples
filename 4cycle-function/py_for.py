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

# iterate with index
hello = "Hello"
for index, value in enumerate(hello):
    print(f"index {index}: value {value}")