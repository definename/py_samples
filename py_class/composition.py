class Bill():
    def __init__(self, description):
        self.__description = description
    @property
    def desc(self):
        return self.__description

class Tail():
    def __init__(self, length):
        self.__length = length
    @property
    def length(self):
        return self.__length

class Duck():
    def __init__(self, bill, tail):
        self.__bill = bill
        self.__tail = tail
    @property
    def about(self):
        return "This duck has a " + self.__bill.desc + " bill and a " + self.__tail.length + " tail"

print(Duck(Bill("wide orange"), Tail("long")).about)