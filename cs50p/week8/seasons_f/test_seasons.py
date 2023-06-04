from seasons import convert
import pytest


def test_nondigit():
    with pytest.raises(ValueError):
        convert("!@#")

def test_over():
    with pytest.raises(TypeError):
        convert("2025-01-01")

def test_negative():
    with pytest.raises(ValueError):
        convert("-2021-01-01")