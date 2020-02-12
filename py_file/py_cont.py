#! /usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

ddict = {"a":1, "b":2, "c":3}
llist = [1, 2, 3]

fname = "obj.dat"
with open(file=fname, mode="wt") as f:
    f.write(f"{ddict}${llist}")

with open(file=fname, mode="r") as f:
    line = f.readline()
    log.debug(f"line read:{line}")
    parts = line.split("$")
    obj = [eval(p) for p in parts]
    log.debug(f"obj type:{type(obj)} obj len:{len(obj)}")

    dd = obj[0]
    dd[111] = 4
    log.debug(f"{type(dd)}: {dd}")

    ll = obj[1]
    ll.append(111)
    log.debug(f"{type(ll)}: {ll}")
