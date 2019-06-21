#! /usr/bin/python3

import logging
import decimal

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

log.debug(0.1 + 0.1 + 0.1 - 0.3)

d01 = decimal.Decimal("0.1")
d03 = decimal.Decimal("0.3")
log.debug(d01 + d01 + d01 - d03)

decimal.getcontext().prec = 3
d10 =  decimal.Decimal(10)
d3 =  decimal.Decimal(3)
log.debug(d10 / d3)
