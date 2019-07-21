import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

x = 99

def globan_or_nonlocal():
    x = 100
    def foo():
        log.debug(f"!!!: {x}")
    foo()

def counter(start):
    state = start
    def nested(fruit):
        nonlocal state
        log.debug(f"{fruit}: {state}")
        state += 1
    return nested

def foo0():
    def foo1():
        def foo2():
            log.debug(f">>>: {x}")
        foo2()
    foo1()

def main():
    # Global on non local
    globan_or_nonlocal()

    # Nestaed function and nonlocal
    foo0()

    # Nonlocal counter
    apple = counter(0)
    apple("apple")
    apple("apple")
    apple("apple")

if __name__ == "__main__":
    main()