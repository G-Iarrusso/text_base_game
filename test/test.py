import pytest
import logging
logging.basicConfig()
mylogger = logging.getLogger(__name__)
mylogger.setLevel(logging.INFO)

def func(x):
    return x + 2
class TestClas:
    def func(self, x):
        mylogger.info("info is here")
        return x + 5

    def test_method(self):
        assert 2 == 2
        assert self.func(3) == 8

    def test_2(self):
        assert 1 == 1