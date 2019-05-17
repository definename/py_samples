import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def do():
    log.debug("do!!!")