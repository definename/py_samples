#! /usr/bin/python3

import logging
import struct

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

if __name__ == "__main__":
    # list_items = [0x0001, 0x0002]
    list_items = (0x00ff, 0x00aa)
    log.debug("Origin: {}".format(list_items))

    list_size = len(list_items)
    data_fmt = ">" + "H" * list_size

    log.debug(f"Pack format: {data_fmt}")
    packed = struct.pack(data_fmt, *list_items)

    log.debug(f"Packed data: {packed.hex()}")
    unpacked = struct.unpack(data_fmt, packed)
    log.debug("Unpacked: {}".format(unpacked))

    aa ="100082"
    a = aa.encode()
    log.debug(bytes(a).hex())
    log.debug(f"Decoded: {a.decode()}")
    bb = "SAU16369"
    b = bb.encode()
    log.debug(bytes(b).hex())
    log.debug(f"Decoded: {b.decode()}")
    log.debug(b.decode())
    # 1313030303832
    # 5341553136333639