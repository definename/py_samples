short_list = list((1, 2, 3))
print(short_list)

# Exception handling

pos = 100
try:
    print(short_list[pos])
except:
    print("Need a position between 0 and", len(short_list) - 1, "but got position:", pos)

# Concrete exception handling

while True:
    value = input("Position [q to quit]? ")
    if value == "q":
        break
    try:
        pos = int(value)
        print("list value:", short_list[pos])
    except IndexError as error:
        print("Bad index was given:", pos)
    except Exception as other:
        print("Something else broke:", other)

# Custom exception handling

class InvalidLenghtException(Exception):
    pass

if (len(short_list) > 0):
    raise InvalidLenghtException(len(short_list))


