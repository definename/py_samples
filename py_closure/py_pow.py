import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def foo_pow(x):
    def powpow(y):
        return y ** x
    return powpow

def pow_lambda(x):
    return (lambda y: y ** x)

def main():
    p = foo_pow(2)
    log.debug(f"pow: {p(2)}")
    log.debug(f"pow: {p(3)}")

    m = pow_lambda(2)
    log.debug(f"pow lambda: {m(2)}")
    log.debug(f"pow lambda: {m(3)}")


if __name__ == "__main__":
    main()