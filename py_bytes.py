import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

test = "aa550018000000dcffff0006ffffffff0003ffff000a0007ffff0000f5140d0a"
log.debug(f"test {test}")
log.debug(f"test length: {len(test)}")

log.debug("{:=^100s}".format("!!!"))

insert_block = bytes.fromhex("ffff")
block_size = len(insert_block)
log.debug(f"block size: {block_size}")

raw_test = bytes.fromhex(test)

insert_front = raw_test[0:10]
insert_back = raw_test[10:]
log.debug(f"insert insert_front {insert_front}")
log.debug(f"insert insert_back {insert_back}")
raw_glued = b"".join([insert_front, insert_block, insert_back])
log.debug(f"raw_glued {raw_glued}")
log.debug(f"raw_glued hex {raw_glued.hex()}")

log.debug("{:=^100s}".format("!!!"))

pos = random.randrange(start=0, stop=len(raw_test) - block_size + 1)
log.debug(f"delete at pos: {pos}")
del_front = raw_test[0:pos]
del_back = raw_test[pos + block_size:]
log.debug(f"del_front {del_front.hex()}")
log.debug(f"del_back {del_back.hex()}")
raw_deleted = b"".join([del_front, del_back])
log.debug(f"raw_deleted {raw_deleted.hex()}")
