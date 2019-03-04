def print_and_change_global():
    global animal
    animal = "fruitbear"
    print("animal: ", animal)
    print("local var dictionary:", locals())

animal = "fruitbat"

print_and_change_global()
print(animal)
print("global var dictionary:", globals())