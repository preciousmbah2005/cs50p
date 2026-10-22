from bank import value

def test_bank_value():
    assert value("Hello") == "$0"
    assert value("H") == "$20"
    assert value("Yes") == "$100"