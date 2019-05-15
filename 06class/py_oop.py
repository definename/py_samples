import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


class Base():
    def __init__(self):
        pass

    def foo(self):
        return "Foo"


class Derived(Base):
    def __init__(self):
        super().__init__()

    def bar(self):
        log.debug("Bar")

    def foo(self):
        return super().foo() + " Foo"


def main():
    obj = Derived()
    log.debug("{} {}".format(type(obj), obj.foo()))


if __name__ == "__main__":
    main()
