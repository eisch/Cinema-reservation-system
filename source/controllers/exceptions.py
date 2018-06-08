class RatingNotInRangeError(Exception):
    def __init__(self):
        Exception.__init__(self, "The rating must be between 1 and 10!")


class MovieAlreadyInDatabaseError(Exception):
    def __init__(self):
        Exception.__init__(self, "The movie is in database already!")


class LessThanEightSymbolsError(Exception):
    def __init__(self):
        Exception.__init__(self, "The password is less than 8 symbols")


class MissingCapitalLetterError(Exception):
    def __init__(self):
        Exception.__init__(self, "The password must contain at least one capital letter")


class MissingSpecialSymbolError(Exception):
    def __init(self):
        Exception.__init__(self, "The password must contain at least one special symbol")


class InvalidMovieIdTypeError(Exception):
    def __init__(self):
        Exception.__init__(self, "The movie_id's type is invalid")


class MovieNotInDataBaseError(Exception):
    def __init__(self):
        Exception.__init__(self, "The movie doesn't exists in database")


class ProjectionInDataBaseError(Exception):
    def __init__(self):
        Exception.__init__(self, "The projection exists in database")


class InvalidDateError(Exception):
    def __init__(self):
        Exception.__init__(self, "The date format is invalid!")


class InvalidTimeError(Exception):
    def __init__(self):
        Exception.__init__(self, "The time format is invalid!")


class TooMuchArgumentsError(Exception):
    def __init__(self):
        Exception.__init__(self, "Too many arguments for this function")
