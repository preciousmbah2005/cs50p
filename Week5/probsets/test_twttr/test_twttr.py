from twttr import shorten


def test_vowel_removed():
    assert shorten("word") == "wrd"
    assert shorten("Precious") == "Prcs"