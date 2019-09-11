#!/usr/bin/python3

import logging
from proto import test_proto2_pb2 as tp2

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

if __name__ == "__main__":
    try:
        log.debug("Serialize...")
        test = tp2.Test()

        tm1 = tp2.Test_m1()
        tm1.i = 99
        test.m1.CopyFrom(tm1)

        item_str = test.items.add()
        item_str.key = tp2.Item.DATA1
        item_str.str = "stringpayload"

        item_int = test.items.add()
        item_int.key = tp2.Item.DATA2
        item_int.i32 = 123

        log.debug(f"Test origin:{test}")
        raw_data = test.SerializeToString()
        log.debug(f"Serialized test:{raw_data.hex()}")

        test.Clear()
        test.ParseFromString(raw_data)
        log.debug(f"Test deserialized:{test}")

        for item in test.items:
            log.debug(f"key:{item.key}")
            if item.key == tp2.Item.DATA1:
                log.debug(f"value:{item.str}")
            elif item.key == tp2.Item.DATA2:
                log.debug(f"value:{item.i32}")
            else:
                log.debug("Unknown value...")
    except Exception as e:
        log.exception(f"Error occurred:{e}")