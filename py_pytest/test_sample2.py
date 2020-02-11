#! /usr/bin/python3

import logging
log = logging.getLogger(__name__)

class TestClass1:
    def test_three(self, connection):
        ret = connection
        log.debug(ret)
        assert 3 == 3
    
    def test_four(self, connection):
        ret = connection
        log.debug(ret)
        assert 4 == 4