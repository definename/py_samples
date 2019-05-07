# classmethod decorator
class A():
    __count = 0

    def __init__(self):
        A.__count += 1

    def increment(self):
        A.__count += 1

    def decrement(self):
        A.__count -= 1

    @classmethod
    def kids(cls):
        print("A has", cls.__count, "little objects")


a1 = A()
a2 = A()
a3 = A()
A.kids()

a1.increment()
A.kids()

a1.decrement()
A.kids()

# staticmethod decorator


class B():
    @staticmethod
    def ad():
        print("ad")


B.ad()
