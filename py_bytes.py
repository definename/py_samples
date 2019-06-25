import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

test = "aa550018000000dcffff0006ffffffff0003ffff000a0007ffff0000f5140d0a"
insert_block = bytes.fromhex("ffff")
raw_test = bytes.fromhex(test)
log.debug(f"test {raw_test}")
raw_front = raw_test[0:10]
raw_back = raw_test[10:]
log.debug(f"front {raw_front}")
log.debug(f"back {raw_back}")
raw_glued = b"".join([raw_front, insert_block, raw_back])
log.debug(f"glued {raw_glued}")
log.debug(f"raw_glued hex {raw_glued.hex()}")

