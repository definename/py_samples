#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    param = 1.1
    log.debug(f"It works: {type(param)}")
    if (type(param) is float):
        log.debug("Yes it is float")

if __name__ == "__main__":
    main()
