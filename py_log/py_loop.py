#! /usr/bin/python3

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

if __name__ == "__main__":
    try:
        count = 3
        while count:
            log.debug("Looping...")
            count = count - 1
            time.sleep(1)
    except Exception as e:
        log.error(f"Error occurred: {e}", ext_info=True)