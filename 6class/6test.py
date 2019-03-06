class Person():
    def __init__(self, name):
        self.name = name + "!"

    def get_name(self):
        return "Base" + self.name

class ConcretePerson(Person):
    def __init__(self, name):
        self.name = name + "!!"

    def get_name(self):
        return "Derived" + self.name

    def need_a_push(self):
        return "Yeah"

person = Person("Name")
c_person = ConcretePerson("Name")
print("Here is <base> person name:", person.get_name())
print("Here is <derived> person name:", c_person.get_name())
print("Here is derived person need a push:", c_person.need_a_push())