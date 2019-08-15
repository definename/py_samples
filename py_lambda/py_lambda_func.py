#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def foo(param):
    return param + "_exit"

if __name__ == "__main__":
    l  = lambda p: foo(p)
    log.debug(l("do"))
