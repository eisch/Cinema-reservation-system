from controllers.session import session
from model.models import Users
from controllers.password_hash import HashPassword
from controllers.validator import PasswordValidator
from datetime import datetime


def user_exists(func):
    def find_user(cls, username, password):
        users = session.query(Users.username).filter(Users.username == username).all()
        if len(users) == 0:
            return func(cls, username, password)
        else:
            hashed_password = HashPassword.hash_password(password)
            for user in users:
                if not HashPassword.check_password(hashed_password, password):
                    return func(username, password)
    return find_user


def validate_password(func):
    def val_pass(cls, password):
        PasswordValidator.check_all(password)
        return func(cls, password)
    return val_pass


def log_info(func):
    def save_into_file(cls, username, string):
        with open('info_reservations.txt', 'a') as f:
            f.write(f"{str(datetime.now())}\n")
            f.write(f"Username: {username}\n")
            f.write(f"{string}\n\n")
        return func(cls, username, string)
    return save_into_file
