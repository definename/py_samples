#!/usr/bin/python3

import logging
import urllib
from urllib.parse import urlparse
from urllib.parse import urlsplit

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def test_string_split(test_path):
    log.debug("................................")
    log.debug(test_path)

    path_res = test_path.split("#", 1)
    log.debug(path_res)
    test_path = path_res[0]
    log.debug(test_path)

    path_res = test_path.split("?", 1)
    log.debug(path_res)
    test_path = path_res[0]
    log.debug(test_path)

def test_urlparse(test_path):
    log.debug("................................")
    res = urlparse(test_path)
    log.debug(res)
    res = urllib.parse.parse_qs(res.query)
    log.debug(res)
    chunk = res.get("chunk", None)
    log.debug(f"chunk:{chunk}")
    sleep = res.get("sleep", None)
    log.debug(f"sleep:{sleep}")
    disconnect = res.get("disconnect", None)
    log.debug(f"disconnect:{disconnect}")


def test_urlsplit(test_path):
    log.debug("................................")
    res= urlsplit(test_path)
    log.debug(res)


def main():
    test_path = "/scripts/run_something.sh?chunk=2048&sleep=2&disconnect=2#fragment"
    test_string_split(test_path)
    test_urlparse(test_path)
    test_urlsplit(test_path)

    test_path = "/scripts/run_something.sh?chunk=""&sleep&disconnect=2#fragment"
    test_urlparse(test_path)
    test_path = "/scripts/run_something.sh"
    test_urlparse(test_path)



if __name__ == "__main__":
    main()