#!/usr/bin/python3

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

cv =  threading.Condition()
done_list = {}

def wait_done(done_id):
    log.debug(f"Do... {done_id}")
    with cv:
        while done_list[done_id] != True:
            if cv.wait(timeout=2.0) == False:
                log.debug(f"Timeout expired...{done_id}")
    log.debug(f"Done... {done_id}")

def set_done():
    with cv:
        for key in done_list.keys():
            done_list[key] = True
            cv.notify_all()

def main():
    thread_list = []
    for index in range(2):
        done_list[index] = False
        thread_list.append(threading.Thread(target=wait_done, args=(index,)))

    for t in thread_list:
        t.start()
        time.sleep(1.0)

    while True:
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.debug("Stop...")
        set_done()
    except Exception as e:
        log.exception(f"Error occurred:{e}")
