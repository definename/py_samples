class Person():
    def __init__(self, name):
        print("__init__ Person")
        self.name = name + "!"

class ConcretePerson(Person):
    def __init__(self, name):
        print("__init__ ConcretePerson")
        self.name = name + "!!"

    def get_name(self):
        return "Derived" + self.name

person = Person("Name")
c_person = ConcretePerson("Name")
print("Here is <base> person name:", person.name)
print("Here is <derived> person name:", c_person.get_name())
print("The same as previous call: Here is <derived> person name:", ConcretePerson.get_name(c_person))
print()

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        print("__init__ EmailPerson")
        self.email = email

e_person = EmailPerson("Name", "name@gmail.com")
print("EmailPerson name:", e_person.name, "email:", e_person.email)
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

# classmethod decorator
class A():
    __count = 0
    def __init__(self):
        A.__count += 1

    @classmethod
    def kids(cls):
        print("A has", cls.__count, "little objects")

a1 = A()
a2 = A()
a3 = A()
A.kids()

# staticmethod decorator
class B():
    @staticmethod
    def ad():
        print("ad")

B.ad()