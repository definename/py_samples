#! /usr/bin/python3

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

fmt = logging.Formatter("%(levelname)s:%(message)s")

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(fmt)

log.addHandler(ch)

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return '[%s] %s' % (self.extra["extra_param"], msg), kwargs


def main():
    adapter = CustomAdapter(log, {"extra_param":999})
    adapter.debug("msg")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(f"Error occurred: {e}")