from plates import is_valid


def test_startnum():
    assert is_valid("123456") == False

def test_length():
    assert is_valid("1234567") == False
    assert is_valid("1") == False

def test_middlenum():
    assert is_valid("AA11AA") == False
    assert is_valid("AAAA01") == False

def test_symbols():
    assert is_valid("!@#$%^") == False
    assert is_valid("AA  AA") == False

def test_valid():
    assert is_valid("AA1234") == True