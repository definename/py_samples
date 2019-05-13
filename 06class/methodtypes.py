import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


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
        log.debug("A has {} little objects".format(cls.__count))


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
        log.debug("ad")


B.ad()
