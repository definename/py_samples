#! /usr/bin/python3.6

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def func(x: "x coordinate" = 0, y : "y coordinate" = 1, z: "z coordinate" = 2) -> int:
    return x + y + z


def main():
    log.debug(f"Res: {func()}")
    for arg in func.__annotations__:
        log.debug(f"{arg} => {func.__annotations__[arg]}")

if __name__ == "__main__":
    main()