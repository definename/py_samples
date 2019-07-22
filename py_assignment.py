#! /usr/bin/python3

import logging
import time

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
    is_seed = 1
    seed = is_seed or time.time()
    log.debug(seed)


if __name__ == "__main__":
    main()