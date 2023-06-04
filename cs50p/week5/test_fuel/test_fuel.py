import pytest
from fuel import convert

def test_negative():
    with pytest.raises(ValueError):
        convert("-1/2")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_nondigit():
    with pytest.raises(ValueError):
        convert("asd")
    with pytest.raises(ValueError):
        convert("!@#")

def test_positive():
    assert convert("1/2") == 50