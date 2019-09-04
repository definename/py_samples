#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

if __name__ == "__main__":
    modname = "imported"
    imported = __import__(modname)
    imported.imported_func()