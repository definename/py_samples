#! /usr/bin/python3

import logging
import hmac
import hashlib

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    # hmac_key = bytes([112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131])
    hmac_key = bytes.fromhex("707172737475767778797a7b7c7d7e7f80818283")

    # text = bytes([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100])
    text = b"Hello World"

    digest = hashlib.sha1

    hmac_obj = hmac.new(key=hmac_key, msg=text, digestmod=digest)
    log.debug("Hmac key size:{}".format(len(hmac_key)))
    log.debug("Hmac size:{}".format(hmac_obj.digest_size))
    hmc_res = hmac_obj.digest()
    log.debug("Hmac:{} size:{}".format(hmc_res.hex(), len(hmc_res)))

if __name__ == "__main__":
    main()
