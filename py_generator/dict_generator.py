#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    word = "SPAM"
    d = { letter: letter*2 for letter in word}
    log.debug(d)

if __name__ == "__main__":
    main()


