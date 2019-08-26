#!/usr/bin/python3
import logging
import argparse

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", type=int, nargs="+", help="Positional args")
    parser.add_argument("--strings", type=str, nargs="*", help="Optional args")
    parser.add_argument("--foo", help="Optional arg")

    args_str = "1 2 3 --strings 11 22 33 --foo fff"
    args = parser.parse_args(args_str.split())

    log.debug(f"integers: {args.integers}")
    if args.strings:
        log.debug(f"strings: {args.strings}")
    if args.foo:
        log.debug(f"foo: {args.foo}")

if __name__ == "__main__":
    main()