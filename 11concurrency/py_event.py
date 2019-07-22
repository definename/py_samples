#! /usr/bin/python3

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

TIMEOUT = 1

def foo():
    ret = None
    log.debug(time.time())
    return ret

def main():
        global TIMEOUT
        ticker = threading.Event()
        while not ticker.wait(TIMEOUT):
            TIMEOUT = foo()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.error("Keyboard interrupted")
    except Exception as e:
        log.error(f"Error occurred: {e}")