#!/usr/bin/python3
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def test_func_args(one, two, three):
    log.debug(f"{one} {two} {three}")

def test_func_kwargs(*, w=0, a, b, c=99):
    log.debug(f"{w} {a} {b} {c}")

def test_func(*args, **kwargs):
    log.debug(f"{args}")
    log.debug(f"{kwargs}")
    test_func_args(*args)
    test_func_kwargs(w="www", **kwargs)


def main():
    test_func(1, 2, 3, a=11, b=22, c=33)

if __name__ == "__main__":
    main()
