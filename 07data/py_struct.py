import struct
import logging

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s - %(message)s", level=logging.DEBUG)
log = logging.getLogger()

data = 1
log.debug("= {} native".format(struct.pack("=1I", data)))
log.debug("@ {} native".format(struct.pack("@1I", data)))
log.debug("< {} little".format(struct.pack("<1I", data)))
log.debug("> {} big".format(struct.pack(">1I", data)))
log.debug("! {} network (= big)".format(struct.pack("!1I", data)))


log.debug("")

num = 1
l_packed = struct.pack("<1I", num)
log.debug("{:>20} :l packed".format(l_packed.hex()))
log.debug("{:>20x} :l unpacked".format(struct.unpack("<1I", l_packed)[0]))
log.debug("{:>20x} :b unpacked".format(struct.unpack(">1I", l_packed)[0]))

log.debug("")

b_packed = struct.pack(">1I", num)
log.debug("{:>20} :b packed".format(b_packed.hex()))
log.debug("{:>20x} :l unpacked".format(struct.unpack("<1I", b_packed)[0]))
log.debug("{:>20x} :b unpacked".format(struct.unpack(">1I", b_packed)[0]))