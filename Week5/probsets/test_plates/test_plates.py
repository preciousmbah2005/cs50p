from plates import is_valid

def test_is_valid_input_length():
    assert is_valid("CS50") == True
    assert is_valid("Precious") == False
    assert is_valid("P") == False

def test_is_valid_two_first_letters():
    assert is_valid("CS50") == True
    assert is_valid("C50S") == False
    assert is_valid("5CS0") == False
    assert is_valid("50CS") == False

def test_is_valid_first_letter():
    assert is_valid("0C50") == False

def test_is_valid_letter_after_number():
    assert is_valid("CS50") == True
    assert is_valid("C50S") == False

def test_is_valid_puntuation():
    assert is_valid("CS.0") == False