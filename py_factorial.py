import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="Number", required=True)
    args = parser.parse_args()

    result = 1
    for i in range(1, args.n + 1):
        result = result * i
        log.debug("{}".format(result))
    log.debug("Factorial:{}".format(result))

if __name__ == "__main__":
    main()