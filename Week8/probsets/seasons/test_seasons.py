from datetime import date
import pytest
from seasons import calculate_minutes


def test_one_day():
    assert calculate_minutes("2000-01-01", date(2000, 1, 2)) == 1440


def test_leap_year():
    assert calculate_minutes("2020-02-28", date(2020, 3, 1)) == 2880


def test_multiple_days():
    assert calculate_minutes("2000-01-01", date(2000, 1, 11)) == 14400


def test_invalid_date():
    with pytest.raises(ValueError):
        calculate_minutes("January 1, 2000")