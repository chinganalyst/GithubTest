import pytest
from utils import add
from utils import substract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_substract_simple():
    assert substract(5, 3) == 2
    assert substract(0, 0) == 0
    assert substract(-1, -2) == 1
