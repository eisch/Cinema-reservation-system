import uuid
import hashlib


class HashPassword:
    def __init__(self, password):
        self.password = HashPassword.hash_password(password)

    @classmethod
    def hash_password(cls, password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return (hashlib.sha256(salt.encode() +
                password.encode()).hexdigest() + ':' + salt)

    @classmethod
    def check_password(cls, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return (password == hashlib.sha256(salt.encode() +
                user_password.encode()).hexdigest())