from model.models import Users
from .session import session
from .decorators import user_exists
from .password_hash import HashPassword


class UserController:
    @classmethod
    @user_exists
    def register(cls, username, password):
        h_password = HashPassword.hash_password(password)
        session.add(Users(username=username, password=h_password))
        session.commit()

    @classmethod
    def user_id_by_username(cls, username):
        result = (session.query(Users.id)
                  .filter(Users.username == username).first())
        return result[0]
