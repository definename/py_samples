#! /usr/bin/python3

import logging
from fractions import Fraction

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

x = Fraction(1, 2)
log.debug(f"x = {x}")
y = Fraction(1, 2)
log.debug(f"y = {y}")
log.debug(f"x + y = {x + y}")
log.debug(f"x * y = {x * y}")
