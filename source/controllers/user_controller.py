from model.models import Users
from .session import session
from .decorators import user_exists, validate_password
from .password_hash import HashPassword
from .exceptions import (LessThanEightSymbolsError,
                         MissingCapitalLetterError,
                         MissingSpecialSymbolError)


class UserController:
    @classmethod
    @user_exists
    def register(cls, username, password):
        try:
            cls.set_password(password)
            h_password = HashPassword.hash_password(password)
            session.add(Users(username=username, password=h_password))
            session.commit()
        except LessThanEightSymbolsError:
            print("The password must contain at least 8 symbols!")
            return True
        except MissingCapitalLetterError:
            print("The password must contain at least one capital letter.")
            return True
        except MissingSpecialSymbolError:
            print("The password must contain at least one special symbol.")
            return True

    @classmethod
    def user_id_by_username(cls, username):
        result = (session.query(Users.id)
                  .filter(Users.username == username).first())
        return result[0]

    @classmethod
    @validate_password
    def set_password(cls, password):
        return password
