#!/usr/bin/python3

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

cv = threading.Condition()

def thread_handler():
    while True:
        log.debug("Here is thread")
        with cv:
            if cv.wait(10) == True:
                log.debug("Exit...")
                break

def main():
    t = threading.Thread(target=thread_handler)
    # t.daemon = True
    t.start()
    t.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        with cv:
            cv.notify_all()
        log.error("Keyboard interrupted...")
    except Exception as e:
        log.error(f"Error occurred:{e}")