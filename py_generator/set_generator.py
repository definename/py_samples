#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    s = { num for num in range(1, 5) if num % 2 > 0 }
    log.debug(f"{type(s)} {s}")

if __name__ == "__main__":
    main()


