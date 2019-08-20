#! /usr/bin/python3

import logging
log = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename="logfile.log", level=logging.DEBUG, filemode="w", format="%(levelname)s %(asctime)s:%(message)s")
    
    logging.debug("msg")
    logging.info("msg")
    logging.warning("msg")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.debug("Error occurred: {e}")