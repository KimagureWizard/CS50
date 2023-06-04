from twttr import shorten

def test_nonvowel():
    assert shorten("qwrty") == "qwrty"

def test_vowel():
    assert shorten("aeiou") == ""

def test_num():
    assert shorten("12345") == "12345"

def test_symbol():
    assert shorten("!@#$%") == "!@#$%"