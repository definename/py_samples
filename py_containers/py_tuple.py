import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

empy_tuple = ()
log.debug(empy_tuple)

tuple1 = "one",
log.debug(tuple1)

tuple2 = "one", "two"
log.debug(tuple2)

tuple3 = (1, 2, 3)
log.debug(tuple3)

log.debug("0x{:04x} 0x{:04x} 0x{:04x}".format(*tuple3))
t1, t2, t3 = tuple3
log.debug(">>> {} {} {}".format(t1, t2, t3))

t1, t2 = t2, t1
log.debug("!!! {} {} {}".format(t1, t2, t3))

originList = ["list1", "list2", "list3"]
log.debug("originList: {}".format(originList))
originTuple = (1, 2, 3, originList)
log.debug("originTuple: {}".format(originTuple))

try:
    originTuple[0] = 999
except TypeError as e:
    log.error("Unbale to change tuple container: {}".format(e))

originTuple[3][0] = "changed"
log.debug("But we can change list which was passed to the tuple: {}".format(originTuple))

# Test unpack tuple automaticaly.
cmd, = (1,)
log.debug(cmd)
