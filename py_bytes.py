import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

test = "aa550018000000dcffff0006ffffffff0003ffff000a0007ffff0000f5140d0a"
log.debug(f"test {test}")

log.debug("{:=^50s}".format("INSERT"))
raw_block = bytes.fromhex("f0f0")
log.debug(f"raw_block {raw_block.hex()}")
block_size = len(raw_block)
log.debug(f"block size: {block_size}")

raw_test = bytes.fromhex(test)
log.debug(f"raw_test length: {len(raw_test)}")

insert_front = raw_test[0:10]
insert_back = raw_test[10:]
log.debug(f"insert insert_front {insert_front}")
log.debug(f"insert insert_back {insert_back}")
raw_glued = b"".join([insert_front, raw_block, insert_back])
log.debug(f"raw_glued {raw_glued}")
log.debug(f"raw_glued hex {raw_glued.hex()}")

log.debug("{:=^50s}".format("DELETE"))
pos = random.randrange(start=0, stop=len(raw_test) - block_size + 1)
log.debug(f"delete at pos: {pos}")
del_front = raw_test[0:pos]
del_back = raw_test[pos + block_size:]
log.debug(f"del_front {del_front.hex()}")
log.debug(f"del_back {del_back.hex()}")
raw_deleted = b"".join([del_front, del_back])
log.debug(f"raw_deleted {raw_deleted.hex()}")

log.debug("{:=^50s}".format("XOR"))
pos = random.randrange(start=0, stop=len(raw_test) - block_size + 1)
log.debug(f"xor pos: {pos}")
raw_chunk = raw_test[pos:pos + block_size]
log.debug(f"raw_chunk {raw_chunk.hex()}")

chunk_xored = [each ^ key for each, key in zip(raw_chunk, raw_block)]
log.debug(f"chunk_xored: {bytes(chunk_xored).hex()}")

log.debug("{:=^50s}".format("XOR with bytes"))
log.debug(b"".join([raw_test[0:pos], bytes(chunk_xored), raw_test[pos+block_size:]]).hex())

log.debug("{:=^50s}".format("XOR with list"))
byte_list = list(raw_test)
byte_list[pos:pos+block_size] = list(chunk_xored)
log.debug(bytes(byte_list).hex())

log.debug("{:=^50s}".format("XOR with bytearray"))
byte_array = bytearray(raw_test)
byte_array[pos:pos+block_size] = chunk_xored
log.debug(byte_array.hex())

log.debug("{:=^50s}".format("chunk"))
chunk = raw_test
raw_test = b""
log.debug(raw_test)
log.debug(chunk)