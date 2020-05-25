from main import get_user_details, is_valid_credentials

def test_correct_user_and_password_return_secret():
    user = "robert"
    password = "password123"
    assert is_valid_credentials(user, password)


def test_incorrect_user_return_get_lost():
    user = "notrobert"
    password = "password123"
    assert not is_valid_credentials(user, password)


def test_incorrect_password_return_get_lost():
    user = "robert"
    password = "ppassword123"
    assert not is_valid_credentials(user, password)
