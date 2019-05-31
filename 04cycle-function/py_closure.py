import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# closure

def talk(subject):
    def inner():
        print("We are talking on '%s'" % subject)
    return inner

a = talk("Subject1")
b = talk("Subject2")

print(type(a))
print(type(b))
a()
b()

# change closure
def f(x):
    def g(y):
        return x * y
    def set_x(a):
        nonlocal x
        x = a
    g.set_x = set_x
    return g

g = f(2)
print(g(10))

g.set_x(4)
print(g(10))

class EngineAsync():
    def __init__(self):
        self.__sn = None

    def set_serial(self, sn):
        self.__sn = sn
        log.debug("set_serial: {}".format(self.__sn))
    
    def get_serial(self):
        log.debug("get_serial: {}".format(self.__sn))
        return self.__sn

class Engine(EngineAsync):
    def __init__(self):
        super().__init__()
        self.__name = "name"

    def __quard(self, func):
        def inner(*args, **kwargs):
            log.debug("Decorated")
            return func(*args, **kwargs)
        return inner

    def set_serial(self, sn):
        self.__quard(super().set_serial)(sn)
    
    def get_serial(self):
        return self.__quard(super().get_serial)()

def main():
    engine = Engine()
    engine.set_serial(123321)
    log.debug(engine.get_serial())

if __name__ == "__main__":
    main()