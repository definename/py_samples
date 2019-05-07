class Person():
    def __init__(self, name):
        print("__init__ Person")
        self.name = name
        self.__secure = "BaseSecure"

    @property
    def secure(self):
        return self.__secure


class ConcretePerson(Person):
    def __init__(self, name, email):
        print("__init__ ConcretePerson")
        super().__init__(name)
        self.email = email
        print("__init__ ConcretePerson {}".format(self.secure))


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
    def __init__(self, name, args=None):
        self.__name = name
        self.__args = args

    @property
    def name(self):
        print("inside get_name")
        return self.__name

    @property
    def args(self):
        print("inside get_name")
        return self.__args

    @args.setter
    def args(self, args):
        print("inside set_args")
        self.__args = args

    @name.setter
    def name(self, name):
        print("inside set_name")
        self.__name = name


carrot = Carrot("Name", args=[1, 2, 3])
carrot.name = "Green Carrot"
print("Carrot name:", carrot.name)
carrot.args = [4, 5, 6]
print("Carrot name:", carrot.args)
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
