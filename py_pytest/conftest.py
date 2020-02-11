import pytest

import logging
logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger(__name__)

# @pytest.fixture(scope="module") # fixture is called once per test module
@pytest.fixture(scope="session") # fixture is called once per test session
def connection():
    log.debug("Fixture called")
    return "111"