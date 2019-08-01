#! /usr/bin/python3.6

import signal
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

if __name__ == "__main__":
    log.debug(f"{signal.SIGINT.name}=> {signal.SIGINT.value}")
    log.debug(f"{signal.SIGTERM.name}=> {signal.SIGTERM.value}")