from bank import value


def test_bank_value():
    assert value("Hello") == "$0"
    assert value("H") == "$20"
    assert value("Yes") == "$100"


def test_bank_value_hello_prefix():
    assert value("Hello there") == "$0"
    assert value("Hello, Newman") == "$0"


def test_bank_value_other_h_greetings():
    assert value("Hi") == "$20"
    assert value("Howdy") == "$20"


def test_bank_value_other_greetings():
    assert value("Good morning") == "$100"
    assert value("What's up?") == "$100"