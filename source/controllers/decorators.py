from controllers.session import session
from model.models import Users
from controllers.password_hash import HashPassword
from controllers.validator import PasswordValidator


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
    def val_pass(password):
        PasswordValidator.check_all(password)
        return func(password)
    return val_pass


def log_info(func):
    def save_into_file(cls, username):
        with open('info_reservations.txt', 'a') as f:
            f.write('\n')
            f.write(username)
            f.write('\n')
        return func(cls, username)
    return save_into_file
