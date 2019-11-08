#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class Instance:
    pass

def main():
    one = Instance()
    two = Instance()
    id_one = id(one)
    id_two = id(two)
    log.debug(f"{id_one} {id_two} {id_one==id_two}")

if __name__ == "__main__":
    main()
