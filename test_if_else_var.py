import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

if __name__ == "__main__":
    if True:
        trigger = True
    else:
        trigger = False
    log.debug(f"{trigger}")