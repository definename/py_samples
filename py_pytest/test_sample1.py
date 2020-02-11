#! /usr/bin/python3

import logging
log = logging.getLogger(__name__)

def test_connection(connection):
    ret = connection
    log.debug(ret)

class TestClass1:
    def test_one(self, connection):
        ret = connection
        log.debug(ret)
        assert 1 == 1

    def test_two(self, connection):
        ret = connection
        log.debug(ret)
        assert 2 == 2