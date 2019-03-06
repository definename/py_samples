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
        self.hidden_name = name

    def get_name(self):
        print("inside get_name")
        return self.hidden_name

    def set_name(self, name):
        print("inside set_name")
        self.hidden_name = name

    name = property(get_name, set_name)

duck = Duck("Name")
duck.name = "Donald Duck"
print("Duck name:", duck.name)
print()

class Carrot():
    def __init__(self, hidden_name):
        self.hidden_name = hidden_name

    @property
    def name(self):
        print("inside get_name")
        return self.hidden_name

    @name.setter
    def name(self, hidden_name):
        print("inside set_name")
        self.hidden_name = hidden_name

carrot = Carrot("Name")
carrot.name = "Green Carrot"
print("Carrot name:", carrot.name)
print()


# Properties can be calculated at runtime.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        print("inside diameter")
        return self.radius * 2

circle = Circle(10)
print("Diameter: ", circle.diameter)