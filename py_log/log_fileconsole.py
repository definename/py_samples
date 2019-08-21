#! /usr/bin/python3

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

fmt = logging.Formatter("%(name) - s%(levelname)s %(asctime)s:%(message)s")

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(fmt)

fh = logging.FileHandler(filename="fileconsole.log", mode="a")
fh.setLevel(logging.DEBUG)
fh.setFormatter(fmt)

log.addHandler(fh)
log.addHandler(ch)


def main():
    # logging.basicConfig(filename="logfile.log", level=logging.DEBUG, filemode="w", format="%(levelname)s %(asctime)s:%(message)s")
    
    log.debug("msg")
    log.info("msg")
    log.warning("msg")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(f"Error occurred: {e}")