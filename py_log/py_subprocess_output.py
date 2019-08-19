#! /usr/bin/python3

import threading
import logging
import subprocess
import time
import signal
import io

logging.basicConfig(filename="pylog.log",
                    level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def work_after_child_is_terminated():
    proc = subprocess.Popen(args=["./py_loop.py"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True
                            )
    log.debug(f"Proc pid: {proc.pid}")

    x = None
    while x == None:
        proc_out, proc_error = proc.communicate()
        log.debug(f"{proc_out, proc_error}")
        x = proc.poll()

if __name__ == "__main__":
    try:
        work_after_child_is_terminated()
    except KeyboardInterrupt:
        log.debug("Exit...")
    except Exception as e:
        log.error(f"Error occurred: {e}", exc_info=True)