
import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20


def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar(2.5)

    with pytest.raises(ValueError):
        Jar("10")


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(3)
    assert jar.size == 8


def test_invalid_deposit():
    jar = Jar(5)
    jar.deposit(4)

    with pytest.raises(ValueError):
        jar.deposit(2)

    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(3)

    assert jar.size == 4


def test_invalid_withdraw():
    jar = Jar(5)
    jar.deposit(2)

    with pytest.raises(ValueError):
        jar.withdraw(3)

    with pytest.raises(ValueError):
        jar.withdraw(-1)
