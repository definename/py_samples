#!/usr/bin/python3
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

import testpacket1.testmodule1 as tm1
import testpacket1.testmodule2 as tm2

if __name__ == "__main__":
    try:
        log.debug(tm1.module_name)
        log.debug(tm2.module_name)
    except Exception as e:
        log.exception(f"Error occurred: {e}")