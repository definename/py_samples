#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    word = "SPAM"
    d = { letter: letter*2 for letter in word}
    log.debug(d)

    dd = {x : y for x in [1, 2, 3] for y in [4, 5, 6]}
    log.debug(f"Dict doesn't allow duplicates: {dd}")

if __name__ == "__main__":
    main()


