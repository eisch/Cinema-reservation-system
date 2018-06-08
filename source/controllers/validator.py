
from controllers.exceptions import (MovieAlreadyInDatabaseError,
                                    LessThanEightSymbolsError,
                                    MissingCapitalLetterError,
                                    MissingSpecialSymbolError,
                                    MovieNotInDataBaseError,
                                    ProjectionInDataBaseError,
                                    InvalidDateError,
                                    InvalidTimeError,
                                    InvalidMovieIdTypeError,
                                    TooMuchArgumentsError,
                                    RatingNotInRangeError)
from datetime import date, time


class Validator:
    def check_data_valid_type(value, value_type):
        if type(value) is not value_type:
            raise ValueError


class MovieValidator(Validator):
    @classmethod
    def check_if_movie_is_in_db(cls, result):
        if result:
            raise MovieAlreadyInDatabaseError()

    @classmethod
    def check_rating_in_range(cls, rating):
        if rating < 1.0 and rating > 10.0:
            raise RatingNotInRangeError()

    @classmethod
    def check_all(cls, name, rating):
        cls.check_data_valid_type(name, str)
        cls.check_data_valid_type(rating, float)
        cls.check_rating_in_range(rating)


class PasswordValidator(Validator):
    @classmethod
    def check_eight_symbols(cls, password):
        if len(password) < 8:
            raise LessThanEightSymbolsError()

    @classmethod
    def check_capital_letter(cls, password):
        if not any(letter.isupper() for letter in password):
            raise MissingCapitalLetterError()

    @classmethod
    def check_special_symbol(cls, password):
        special_symbols = ['"', "\\", " "]
        special_symbols += [symbol for symbol in
                            "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"]
        if not any(symbol in special_symbols for symbol in password):
            raise MissingSpecialSymbolError()

    @classmethod
    def check_all(cls, password):
        PasswordValidator.check_eight_symbols(password)
        PasswordValidator.check_capital_letter(password)
        PasswordValidator.check_special_symbol(password)
        return True


class ProjectionValidator(Validator):
    @classmethod
    def check_movie_id_type(cls, movie_id):
        flag = None
        try:
            a = int(movie_id)
            assert (a > 0)
            flag = True
        except ValueError:
            flag = False
        finally:
            return flag

    @classmethod
    def check_movie_id(cls, movie_id):
        if not ProjectionValidator.check_movie_id_type(movie_id):
            raise InvalidMovieIdTypeError()

    @classmethod
    def check_movie_exists_in_db(cls, info_tuple):
        if not info_tuple:
            raise MovieNotInDataBaseError()

    @classmethod
    def check_projection_in_db(cls, result):
        if result:
            raise ProjectionInDataBaseError()

    @classmethod
    def check_valid_date(cls, user_date):
        flag = None
        try:
            year, month, day = user_date
            new_date = date(year, month, day)
            flag = True
        except ValueError:
            flag = False
        except TypeError:
            flag = False
        finally:
            return flag

    @classmethod
    def check_valid_time(cls, user_time):
        flag = None
        try:
            hour, minutes = user_time
            new_time = time(hour, minutes)
            flag = True
        except ValueError:
            flag = False
        except TypeError:
            flag = False
        finally:
            return flag

    @staticmethod
    def date_and_time_splitter(user_date_and_time, splitter):
        user_date_and_time_list = user_date_and_time.split(splitter)
        if len(user_date_and_time_list) == 1:
            return False
        try:
            return tuple([int(item) for item in user_date_and_time_list])
        except ValueError:
            return False

    @classmethod
    def check_date_in_range(cls, user_date):
        d = ProjectionValidator.date_and_time_splitter(user_date, '-')
        if not d:
            raise InvalidDateError()
        if not ProjectionValidator.check_valid_date(d):
            raise InvalidDateError()

    @classmethod
    def check_time_in_range(cls, user_time):
        t = ProjectionValidator.date_and_time_splitter(user_time, ':')
        if not ProjectionValidator.check_valid_time(t):
            raise InvalidTimeError()

    @classmethod
    def check_len_args(cls, *args):
        if len(*args) > 1:
            raise TooMuchArgumentsError()
