import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


# kids with class method
class A():
    __count = 0

    def __init__(self):
        A.__count += 1

    @classmethod
    def kids(cls):
        log.debug("A has {} little objects".format(cls.__count))


a1 = A()
a2 = A()
a3 = A()
A.kids()


# kids with static method
class B():
    __count = 0

    def __init__(self):
        B.__count += 1

    @staticmethod
    def kids():
        log.debug("B has {} little objects".format(B.__count))


b1 = B()
b2 = B()
b3 = B()
B.kids()
