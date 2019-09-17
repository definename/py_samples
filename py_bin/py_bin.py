#!/usr/bin/python3.6

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("test")

def main():
    ioseq = int("11101111", 2)
    oseq = ioseq & int("f", 16)
    iseq = ioseq & int("f0", 16)
    log.debug("{} {:08b} {}".format(oseq, oseq, bool(oseq)))
    log.debug("{} {:08b} {}".format(iseq, iseq, bool(oseq)))

if __name__ == "__main__":
    main()