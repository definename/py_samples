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

log.debug("=== pack/unpack yymd")

yymd_raw = "20190101"
yymd_parsed = None
try:
    yymd_parsed = datetime.strptime(yymd_raw, r"%Y%m%d")
    log.debug("yymd_parsed yy({}) m({}) d({})".format(yymd_parsed.year, yymd_parsed.month, yymd_parsed.day))
except ValueError as e:
    log.error("Failed to parse date: {}".format(e))
else:
    yymd_packed_big = struct.pack(">HBB", yymd_parsed.year, yymd_parsed.month, yymd_parsed.day)
    log.debug("yymd_packed_big as big-endian {}".format(yymd_packed_big.hex()))
    yymd_packed_little = struct.pack("<HBB", yymd_parsed.year, yymd_parsed.month, yymd_parsed.day)
    log.debug("yymd_packed_big as little-endian {}".format(yymd_packed_little.hex()))

    log.debug("yymd_packed_big len: {}".format(len(yymd_packed_big)))
    yymd = (yy, m, d) = struct.unpack(">HBB", yymd_packed_big)
    log.debug("yymd_unpacked yy({}) m({}) d({})".format(yymd[0], yymd[1], yymd[2]))

log.debug("=== pack/unpack bb")

bb_raw = struct.pack("BB", 0, 3)
log.debug(bb_raw.hex())

log.debug("=== parse invalid format")

try:
    invalid_format = bytes.fromhex("00110020ffff0005ffff0001000000000007ffff004849")
    valid_format= bytes.fromhex("00110020ffff0005ffff0001000a000000000007ffff0000")
    log.debug(f"invalid frame size: {len(invalid_format)}")
    log.debug(f"valid frame size: {len(valid_format)}")
    log.debug(list(invalid_format[:1]))
    struct.unpack(">12H", invalid_format[:24])
except Exception as e:
    log.error(f"Error occurred: {e}")