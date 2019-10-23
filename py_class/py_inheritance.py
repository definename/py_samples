#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class A1:
    def __init__(self, who):
        self.who1 = who

class A2:
    def __init__(self, who):
        self.who2 = who

class A(A1, A2):
    def __init__(self, whoI, whoYou):
        A1.__init__(self, whoI)
        A2.__init__(self, whoYou)

    def who(self):
        log.debug(f"{self.who1} and {self.who2}")

def main():
    a = A("I", "You")
    a.who()

if __name__ == "__main__":
    main()