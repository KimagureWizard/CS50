from bank import value


def test_h():
    assert value("Hat") == 20

def test_hello():
    assert value("Hello") == 0

def test_num():
    assert value("12345") == 100

def test_symbol():
    assert value("!@#$%") == 100

def test_str():
    assert value("asd") == 100