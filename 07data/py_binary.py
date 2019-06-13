import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

bList = [1, 2, 3, 255]
theBytes = bytes(bList)
log.debug("{}".format(theBytes))

theByteArray = bytearray(bList)
log.debug("{}".format(theByteArray))

theByteArray[0] = 127
log.debug("{}".format(theByteArray))

a = 10
log.debug(a << 1)
log.debug(a >> 1)

log.debug("{:08b}".format(3))