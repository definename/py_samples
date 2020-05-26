#! /usr/bin/python3

import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    c = os.getcwd()
    log.debug(c)
    log.debug(os.path.relpath(c))

    n = os.path.join(c, "../../..")
    log.debug(n)
    log.debug(os.path.realpath(n))

if __name__ == "__main__":
    main()