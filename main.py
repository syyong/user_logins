import hashlib

import yaml


def is_valid_credentials(user, password):
    """
    param: user: str
    param: password: str

    return: bool
    """
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    with open('config.yaml', 'r') as file:
        valid_user_password = yaml.safe_load(file)

    for i in valid_user_password:
        if i['username'] == user:
            if i['password_hash'] == password_hash: 
                return True
        return False


def get_user_details():
    user = input("What is your username? ")
    password = input("What is your password? ")
    if is_valid_credentials(user, password):
        print("The deepest, darkest secret.")
    else:
        print("Get lost!")


if __name__ == "__main__":
    get_user_details()