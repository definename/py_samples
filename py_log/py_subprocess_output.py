#! /usr/bin/python3

import threading
import logging
import subprocess
import time
import signal
import io
import os

logging.basicConfig(
                    filename="pylog.log",
                    level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def work_with_communicate_after_proc_terminate():
    proc = subprocess.Popen(args=["./py_loop.py"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True
                            )
    log.debug(f"Proc pid: {proc.pid}")

    x = None
    while x == None:
        proc_out, proc_error = proc.communicate()

        error_lines = proc_error.splitlines()
        for eline in error_lines:
            log.debug(eline)

        out_lines = proc_out.splitlines()
        for oline in out_lines:
            log.debug(oline)

        x = proc.poll()


def work_with_for_stdout():
    cmd = "ls"
    proc = subprocess.Popen(cmd
                            , shell=True
                            , stdin=subprocess.PIPE
                            , stdout=subprocess.PIPE
                            , stderr=subprocess.PIPE
                            , universal_newlines=True
                            # , bufsize=1
                            )

    for line in proc.stdout:
        log.debug(line)


if __name__ == "__main__":
    try:
        work_with_communicate_after_proc_terminate()
        # work_with_for_stdout()
    except KeyboardInterrupt:
        log.debug("Exit...")
    except Exception as e:
        log.error(f"Error occurred: {e}", exc_info=True)
