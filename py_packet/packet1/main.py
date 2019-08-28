import sys
sys.path.append("..")

import logging
from packet import daily

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


def main():
    log.debug(daily.forecast())


if __name__ == "__main__":
    main()
