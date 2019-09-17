#!/usr/bin/python3.6

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("test")

def main():
    # ------------------------------------------------------------- #
    ioseq = int("11101111", 2)
    log.debug("ioseq:{} {:08b}".format(ioseq, ioseq))

    iseq = ioseq & int("f0", 16)
    oseq = ioseq & int("f", 16)
    log.debug("iseq:{} {:08b} {}".format(iseq, iseq, bool(iseq)))
    log.debug("oseq:{} {:08b} {}".format(oseq, oseq, bool(oseq)))

    ioseq = iseq | oseq
    log.debug("ioseq:{} {:08b}".format(ioseq, ioseq))

    # ------------------------------------------------------------- #
    flags = build_flags(nak=True, dup=False, busy=False, control=True)
    log.debug(bin(flags))

def build_flags(*, nak=False, dup=False, busy=False, control=False):
    flags = 0
    flags = int(nak)
    flags = flags << 1

    flags = flags | int(dup)
    flags = flags << 1

    flags = flags | int(busy)
    flags = flags << 1

    flags = flags | int(control)
    return flags

if __name__ == "__main__":
    main()