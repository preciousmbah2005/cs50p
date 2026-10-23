from twttr import shorten


def test_vowel_removed():
    assert shorten("word") == "wrd"
    assert shorten("Precious") == "Prcs"


def test_all_vowels_removed():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""


def test_consonants_preserved():
    assert shorten("rhythm") == "rhythm"
    assert shorten("") == ""


def test_case_and_nonletters_preserved():
    assert shorten("Hello, World! 123") == "Hll, Wrld! 123"
    assert shorten("YELLOW") == "YLLW"