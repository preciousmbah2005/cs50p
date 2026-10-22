# from main import add

# def test_main():
#     assert add(1, 1) == 2

import pytest
from main import UserManager

@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("Mbah_Precious", "preciousmbah@gmail.com") == True
    assert user_manager.get_user("Mbah_Precious") == "preciousmbah@gmail.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("Mbah_Precious", "preciousmbah@gmail.com")
    with pytest.raises(ValueError):
        user_manager.add_user("Mbah_Precious", "mbahprecious@gmail.com")