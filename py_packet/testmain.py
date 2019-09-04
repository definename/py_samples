#!/usr/bin/python3
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

import testpacket1.testmodule1 as tm1
import testpacket2.testmodule3 as tm3

if __name__ == "__main__":
    try:
        log.debug(tm1.test_module1_func())
        log.debug(tm3.test_module3_func())
    except Exception as e:
        log.exception(f"Error occurred: {e}")