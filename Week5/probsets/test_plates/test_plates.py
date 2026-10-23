from plates import is_valid


def test_valid_plate_lengths():
    assert is_valid("AB")
    assert is_valid("ABC123")
    assert not is_valid("A")
    assert not is_valid("ABCDEFG")


def test_plate_starts_with_two_letters():
    assert not is_valid("1ABC")
    assert not is_valid("A1")


def test_numbers_are_at_the_end():
    assert is_valid("CS50")
    assert not is_valid("CS5A")
    assert not is_valid("AB1CD")


def test_first_number_cannot_be_zero():
    assert not is_valid("CS05")
    assert is_valid("CS50")
    assert is_valid("CS10")


def test_plate_has_no_punctuation_or_spaces():
    assert not is_valid("CS.50")
    assert not is_valid("CS 50")
    assert not is_valid("CS,50")
