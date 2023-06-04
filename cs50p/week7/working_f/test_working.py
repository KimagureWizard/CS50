from working import convert
import pytest

def test_nondig():
    with pytest.raises(ValueError):
        convert("a to z")

def test_over():
    with pytest.raises(ValueError):
        convert("10:30 PM to 8:70 AM")