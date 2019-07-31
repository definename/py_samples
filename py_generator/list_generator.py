#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    l = ["a", "b", "c"]
    ll = [a*4 for a in l]
    log.debug(f"{type(ll)} {ll}")

if __name__ == "__main__":
    main()


