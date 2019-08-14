#! /usr/bin/python3

import threading
import logging
import enum

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class Cmd_t(enum.Enum):
    CMD_ONE2 = 1
    CMD_ONE1 = 1
    CMD_TWO = 2

if __name__ == "__main__":
    log.debug(f"{Cmd_t(1)}")
    try:
        Cmd_t(3)
    except ValueError as e:
        log.error(f"Error occured: {e}")