class LessThanEightSymbolsError(Exception):
    def __init__(self):
        Exception.__init__(self, "The password is less than 8 symbols!")


class MissingCapitalLetterError(Exception):
    def __init__(self):
        Exception.__init__(self, "The password must contain at least one capital letter!")


class MissingSpecialSymbolError(Exception):
    def __init(self):
        Exception.__init__(self,
                           "The password must contain at least one special symbol!")


class ProjectionsMissingMovieError(Exception):
    def __init__(self):
        Exception.__init__(self, "Projections doesn't exists in database!")


class InvalidIdTypeError(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid id type!")


class MovieNotInDbError(Exception):
    def __init__(self):
        Exception.__init__(self, "Movie not in database!")


class WantedSeatsMoreThanTicketsError(Exception):
    def __init__(self):
        Exception.__init__(self, "Wanted seats are more than free tickets")


class ProjectionIdNotInMovieProjectionsError(Exception):
    def __init__(self):
        Exception.__init__(self, "This projection id isn't for this movie")


class ReservationIdNotInUserReservationsError(Exception):
    def __init__(self):
        Exception.__init__(self, "There's no reservation with this id for this user")
