from um import count

def test_word():
    assert count("umbrella") == 0

def test_unpper():
    assert count("UMUMUM") == 0

def test_other():
    assert count("Um, thanks, um...") == 2