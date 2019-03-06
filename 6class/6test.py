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