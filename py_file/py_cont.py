#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

d = {"a":1, "b":2, "c":3}
l = [1, 2, 3]

fname = "obj.dat"
with open(file=fname, mode="wt") as f:
    f.write(f"{d}${l}")

with open(file=fname, mode="r") as f:
    line = f.readline()
    parts = line.split("$")
    obj = [eval(p) for p in parts]
    d = obj[0]
    d[111] = 4
    log.debug(f"{type(d)}: {d}")
    l = obj[1]
    l.append(111)
    log.debug(f"{type(l)}: {l}")
