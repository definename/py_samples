import logging
import string
import struct
import random

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


random.seed(a=2)

log.debug("{:=^100s}".format("hexdigits"))
log.debug(string.hexdigits)
for index in range(3):
    log.debug(random.choices(string.hexdigits, k=2))


log.debug("{:=^100s}".format("getrandbits"))
for index in range(3):
    log.debug("{:08b}".format(random.getrandbits(8)))

