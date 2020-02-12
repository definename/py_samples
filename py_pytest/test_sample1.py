#! /usr/bin/python3

import pytest
import logging
log = logging.getLogger(__name__)

input_result_list = [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54)
    ]

@pytest.mark.parametrize("test_input, expected_result", input_result_list)
def test_connection(connection, test_input, expected_result):
    ret = connection
    log.debug(ret)

    test_input_eval = eval(test_input)
    log.debug(f"eval:{test_input_eval}, expected:{expected_result}")
    assert(test_input_eval==expected_result)

class TestClass1:
    def test_one(self, connection):
        ret = connection
        log.debug(ret)
        assert 1 == 1

    def test_two(self, connection):
        ret = connection
        log.debug(ret)
        assert 2 == 2