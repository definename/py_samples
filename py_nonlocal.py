import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def foo0():
    def foo1():
        def foo2():
            log.debug(f">>>>>>>>>>>>: {x}")
        foo2()
    foo1()

x = 99

def main():
    foo0()
    x = 100
    def foo():
        log.debug(f"x: {x}")
    foo()

if __name__ == "__main__":
    main()