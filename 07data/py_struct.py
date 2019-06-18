import struct
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

data = 1
log.debug("= {} native".format(struct.pack("=1I", data)))
log.debug("@ {} native".format(struct.pack("@1I", data)))
log.debug("< {} little".format(struct.pack("<1I", data)))
log.debug("> {} big".format(struct.pack(">1I", data)))
log.debug("! {} network (= big)".format(struct.pack("!1I", data)))


log.debug("===")

num = 1
l_packed = struct.pack("<1I", num)
log.debug("{:>20} :l packed".format(l_packed.hex()))
log.debug("{:>20x} :l unpacked".format(struct.unpack("<1I", l_packed)[0]))
log.debug("{:>20x} :b unpacked".format(struct.unpack(">1I", l_packed)[0]))

log.debug("===")

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

log.debug("===")

data_raw = 12
data_packed = struct.pack("<1H", data_raw)
log.debug("packed: {}".format(data_packed.hex()))
data_unpacket = struct.unpack("<1H", data_packed)
log.debug("unpacked: {}".format(data_unpacket))

log.debug("=== raw date in format yymd (4bytes): e3070612")

yymd_raw = "20150101"
yymd_parsed = None
try:
    yymd_parsed = datetime.strptime(yymd_raw, r"%Y%m%d")
    log.debug("yymd_parsed yy({}) m({}) d({})".format(yymd_parsed.year, yymd_parsed.month, yymd_parsed.day))
except ValueError as e:
    log.error("Failed to parse date: {}".format(e))
else:
    yymd_packed = struct.pack(">HBB", yymd_parsed.year, yymd_parsed.month, yymd_parsed.day)
    log.debug("yymd_packed {}".format(yymd_packed.hex()))

    log.debug("yymd_packed len: {}".format(len(yymd_packed)))
    yymd = (yy, m, d) = struct.unpack(">HBB", yymd_packed)
    log.debug("yymd_unpacked yy({}) m({}) d({})".format(yymd[0], yymd[1], yymd[2]))
