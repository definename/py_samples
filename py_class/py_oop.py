#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


class Base:
    def __init__(self):
        pass

    def foo(self):
        return "Foo"

    def bar(self):
        pass


class DerivedA(Base):
    def __init__(self):
        super().__init__()

    def bar(self):
        return "Bar"

    def foo(self):
        return super().foo() + " FooA"

class DerivedB(Base):
    def __init__(self):
        super().__init__()

    def foo(self):
        return super().foo() + " FooB"


def main():
    l = [DerivedA(), DerivedB()]
    for obj in l:
        log.debug(f"type: {type(obj)}, {obj.foo()}")

    for obj in l:
        try:
            log.debug(f"type: {type(obj)}, {obj.bar()}")
        except AttributeError as e:
            log.error(f"Error corrured: {e}")



if __name__ == "__main__":
    main()
