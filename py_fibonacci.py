import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="Number", required=True)
    args = parser.parse_args()

    first = 0
    second = 1
    log.debug("{}".format(first))
    log.debug("{}".format(second))
    index = 1
    while index in range(1, args.n):
        index += 1
        tmp = second
        second = first + tmp
        first = tmp
        log.debug("{}".format(second))

if __name__ == "__main__":
    main()