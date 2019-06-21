#! /usr/bin/python3

import logging
from decimal import Decimal

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

log.debug(0.1 + 0.1 + 0.1 - 0.3)
log.debug(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))
