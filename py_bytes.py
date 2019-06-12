import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

b = b'0003'
log.debug(b)
log.debug(bytes.fromhex("30303033"))