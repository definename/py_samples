#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    seq = "spam"
    a, *b = seq
    log.debug(f"{a}, {b}")
    *a, b = seq
    log.debug(f"{a}, {b}")
    a, *b, c = seq
    log.debug(f"{a}, {b}, {c}")

if __name__ == "__main__":
    main()