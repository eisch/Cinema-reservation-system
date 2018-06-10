
from controllers.exceptions import (LessThanEightSymbolsError,
                                    MissingCapitalLetterError,
                                    MissingSpecialSymbolError,
                                    ProjectionsMissingMovieError,
                                    InvalidIdTypeError,
                                    MovieNotInDbError,
                                    WantedSeatsMoreThanTicketsError,
                                    ProjectionIdNotInMovieProjectionsError,
                                    ReservationIdNotInUserReservationsError)


class PasswordValidator:
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


class ProjectionValidator:
    @classmethod
    def check_projections_movie(cls, info_tuple):
        if not info_tuple:
            raise ProjectionsMissingMovieError()

    @classmethod
    def check_valid_id(cls, str_id):
        numbers = [str(number) for number in range(0, 11)]
        if not all(symbol in numbers for symbol in str_id):
            raise InvalidIdTypeError()

    @classmethod
    def check_movie_in_db(cls, result):
        if not result:
            raise MovieNotInDbError()

    @classmethod
    def check_if_seats_more_than_tickets(cls, wanted_seats, free_tickets):
        if wanted_seats > free_tickets:
            raise WantedSeatsMoreThanTicketsError()

    @classmethod
    def check_if_projection_id_belongs_to_movie(cls, pr_id, tuple_movie):
        if pr_id not in tuple_movie:
            raise ProjectionIdNotInMovieProjectionsError()

    @classmethod
    def check_if_reservation_id_belongs_to_user(cls, r_id, tuple_reservations):
        if r_id not in tuple_reservations:
            raise ReservationIdNotInUserReservationsError()
