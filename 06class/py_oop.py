import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


class Base():
    def __init__(self):
        pass

    def foo(self):
        log.debug("Foo")


class Derived(Base):
    def __init__(self):
        super().__init__()

    def bar(self):
        log.debug("Bar")

    def foofoo(self):
        return "foofoo"


def main():
    obj = Derived()
    log.debug("{} {}".format(type(obj), obj.foofoo()))


if __name__ == "__main__":
    main()
