import struct
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
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

serial = "12345678912345678"
packed_serial = serial.encode()
log.debug("Packed: {}".format(packed_serial))
unpacked_serial = packed_serial.decode()
log.debug("Unpacked: {}".format(unpacked_serial))

DATA_BYTEORDER = "<"
fmt = "{}B".format(DATA_BYTEORDER)
data_packed = struct.pack(fmt, 255)
log.debug("{} 0x{}".format(data_packed, bytes(data_packed).hex()))

buff = bytes.fromhex("aa55")
un = struct.unpack(">1H", buff[0:2])
log.debug("0x{:04x}".format(un[0]))

data_raw = 12
data_packed = struct.pack("<1H", data_raw)
log.debug("packed: {}".format(data_packed.hex()))
data_unpacket = struct.unpack("<1H", data_packed)
log.debug("unpacked: {}".format(data_unpacket))
