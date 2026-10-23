from fuel import gauge, convert
import pytest


def test_fuel_user_entry_validity():
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("-2/1")


def test_convert_valid_fractions():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("0/4") == 0
    assert convert("4/4") == 100


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_malformed_fractions():
    for fraction in ("1", "1/2/3", "a/2", "1/b", "/2", "2/"):
        with pytest.raises(ValueError):
            convert(fraction)


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
