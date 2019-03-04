# 1
#guess_me = int(input("Enter the value: "))
guess_me = 7

if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else:
    print("just right")

# 2
start = 1
while True:
    if (start < guess_me):
        print("too low")
    elif (start > guess_me):
        print("oops")
    else:
        print("found it!!")
        break
    start += 1

# 3
test_list = [3, 2, 1, 0]
for num in test_list:
    print(num, " ", end="")
print()

# 4 list inclusion
odd_list = [number for number in range(10) if number % 2 > 0]
print("odd_list:", odd_list)

# 5 dict inclusion
square_dict = { key : key**2 for key in range(5) }

for key, value in square_dict.items():
    print("key:", key, "value:", value)

# 6 set inclusion
even_set = { val for val in range(10)}
print("even_set:", even_set)

# 7 generator inclusion
gen_inclusion = ("Got %s" % number for number in range(5))
for thing in gen_inclusion:
    print(thing)

# 7
def good():
    return ["Harry", "Ron", "Hermione"]

print(good())

# 9
def get_even():
    for number in range(1, 10, 2):
        yield number

for count, num in enumerate(get_even(), 1):
    if count == 3:
        print("The third event number is:", num)
        break

# 10 decorator

def test_func():
    print("Here is decorated function!!")

def test(func):
    def new_func(*args, **kwargs):
        print("->Start")
        func(*args, **kwargs)
        print("->End")
    return new_func

dec = test(test_func)
dec()

# 11 Exception

class OopsException(Exception):
    pass

try:
    raise OopsException("Oops msg")
except OopsException as e:
    print("Oops exception has been caught:", e)
except Exception as e:
    print("Exception has been caught:", e)

# 12 zip

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

title_dict = dict()

for key, val in zip(titles, plots):
    title_dict[key] = val

print(title_dict)

# Another way to implement 12 task
print(dict(zip(titles, plots)))