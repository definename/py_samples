#! /usr/bin/python3.6

import logging
import subprocess

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class Legacy:
    cmd = "ls"

    class __Decorator:
        @staticmethod
        def io_decorator(func):
            def inner(*args, **kwargs):
                log.debug(f"== {func.__name__}:")
                func()
            return inner

    @staticmethod
    @__Decorator.io_decorator
    def run_ls_getoutput():
        ret = subprocess.getoutput(Legacy.cmd)
        log.debug(f"Output:\n{ret}")

    @staticmethod
    @__Decorator.io_decorator
    def run_ls_getstatusoutput():
        ret = subprocess.getstatusoutput(Legacy.cmd)
        log.debug(f"Output:\n{ret}")
    
    @staticmethod
    @__Decorator.io_decorator
    def run_ls_call():
        ret = subprocess.call(Legacy.cmd, stdout=subprocess.DEVNULL)
        log.debug(f"Exit code: {ret}")


def main():
    Legacy.run_ls_getoutput()
    Legacy.run_ls_getstatusoutput()
    Legacy.run_ls_call()

if __name__ == "__main__":
    main()