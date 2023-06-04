from numb3rs import validate

def test_neg():
    assert validate("-1.0.0.0") == False
def test_over():
    assert validate("256.0.0.0") == False
def test_nondig():
    assert validate("a.a.a.a") == False