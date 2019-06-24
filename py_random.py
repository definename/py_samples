import logging
import string
import struct
import random

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()


random.seed(a=3)

log.debug("{:=^100s}{}".format("hexdigits", string.hexdigits))
for index in range(3):
    log.debug(random.choices(string.hexdigits, k=2))


log.debug("{:=^100s}".format("getrandbits"))
for index in range(3):
    log.debug("{:08b}".format(random.getrandbits(8)))

log.debug("{:=^100s}{}".format("two digits with replacement", string.digits))
while True:
    pair = random.choices(string.digits, k=2)
    log.debug(f"{pair[0]} {pair[1]}")
    if pair[0] == pair[1]:
        break

