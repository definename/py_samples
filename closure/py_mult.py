import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def foo(x):
    def foofoo(y):
        return y ** x
    return foofoo

def main():
    f = foo(2)
    log.debug(f(2))
    log.debug(f(3))

if __name__ == "__main__":
    main()