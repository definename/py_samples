import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

one_str = "a"
log.debug(one_str)
one = ord(one_str)
log.debug(one)
two = one + 1
log.debug(two)
log.debug(chr(two))