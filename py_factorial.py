import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=int, help="f", required=True)
    args = parser.parse_args()

    result = 1
    for i in range(1, args.f + 1):
        result = result * i
        log.debug("{}".format(result))
    log.debug("Result:{}".format(result))

if __name__ == "__main__":
    main()