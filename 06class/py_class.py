class Person():
    def __init__(self, name):
        print("__init__ Person")
        self.name = name


class ConcretePerson(Person):
    def __init__(self, name, email):
        print("__init__ ConcretePerson")
        super().__init__(name)
        self.email = email


person = ConcretePerson("Concrete", "concrete@gmail.com")
print("Name: {} email: {}".format(person.name, person.email))
print()


class Duck():
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print("inside get_name")
        return self.__name

    def set_name(self, name):
        print("inside set_name")
        self.__name = name

    name = property(get_name, set_name)


duck = Duck("Name")
duck.name = "Donald Duck"
print("Duck name:", duck.name)
# print("Failed to retrieve name:", duck.__name)
print("Duck name lifehack:", duck._Duck__name)
print()


class Carrot():
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("inside get_name")
        return self.__name

    @name.setter
    def name(self, name):
        print("inside set_name")
        self.__name = name


carrot = Carrot("Name")
carrot.name = "Green Carrot"
print("Carrot name:", carrot.name)
print()


# Properties can be calculated at runtime.
# In order to make class attributes private we need to decorate their names with "__" e.g "__name"
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def diameter(self):
        print("inside diameter")
        return self.__radius * 2


circle = Circle(10)
# print("Failed to retrieve radius:", circle.__radius)
print("Radius lifehack:", circle._Circle__radius)
print("Diameter:", circle.diameter)
