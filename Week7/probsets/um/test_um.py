from um import count

def test_case_insensitive():
    assert count("um UM Um") == 3

def test_word_boundaries():
    assert count("yummy umbrella") == 0

def test_multiple_occurrences():
    assert count("um, hello, um, world") == 2

def test_no_um():
    assert count("Hello world") == 0

def test_mixed_text():
    assert count("Um, yummy, UM, umbrella") == 2
