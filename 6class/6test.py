class Person():
    def __init__(self, name):
        self.name = name

class ConcretePerson(Person):
    pass

give_me_a_concrete_person = ConcretePerson("Person")
print("Here is concrete person name:", give_me_a_concrete_person.name)