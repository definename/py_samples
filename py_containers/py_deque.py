#!/usr/bin/python3.6

import logging
import collections

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("test")

def main():
    dq = collections.deque()

    if not dq:
        dq.append(1)

    if dq:
        l = [2, 3, 4]
        dq.extend(l)

    for item in dq:
        log.debug(item)

    while dq:
        log.debug(f"pop:{dq.popleft()}")


if __name__ == "__main__":
    main()
