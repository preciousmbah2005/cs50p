import pytest
from twttr import shorten

def test_vowel_removed(shorten):
    assert shorten("word") == "wrd"
    assert shorten("Precious") == "Prcs"