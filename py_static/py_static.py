#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class SomeClass:
    _block_until = False
    def __init__(self):
        log.debug(self._block_until)

class SomeKid(SomeClass):
    _block_until = True


def main():
    someobj = SomeClass()
    somekid = SomeKid()


if __name__ == "__main__":
    main()
