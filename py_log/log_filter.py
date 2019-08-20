#! /usr/bin/python3

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

fmt = logging.Formatter("%(extra)s:%(message)s")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(fmt)

log.addHandler(ch)

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.extra = "999"
        return True


def main():
    cf = ContextFilter()
    log.addFilter(cf)
    log.debug("Filter")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(f"Error occurred: {e}")