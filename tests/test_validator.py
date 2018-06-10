import sys
sys.path.append('/home/elitsa/projects/week12/monday/source')
from controllers.validator import (PasswordValidator,
                                   ProjectionValidator)
from controllers.exceptions import *
import unittest


class PasswordValidatorTest(unittest.TestCase):
    def test_password_less_than_eight_symbols(self):
        with self.assertRaises(LessThanEightSymbolsError):
            PasswordValidator.check_eight_symbols('abcdefg')

    def test_password_more_or_equal_than_eight_symbols(self):
        PasswordValidator.check_eight_symbols('abcdefgh')

    def test_password_missing_capital_letter(self):
        with self.assertRaises(MissingCapitalLetterError):
            PasswordValidator.check_capital_letter('abcdefgh')

    def test_password_capital_letter(self):
        PasswordValidator.check_capital_letter('abcdefGh')

    def test_password_missing_special_symbol(self):
        with self.assertRaises(MissingSpecialSymbolError):
            PasswordValidator.check_special_symbol('abcdefGh')

    def test_password_special_symbol(self):
        PasswordValidator.check_special_symbol('@bcdefGh')


class ProjectionValidatorTest(unittest.TestCase):
    def test_no_projections_for_movie(self):
        with self.assertRaises(ProjectionsMissingMovieError):
            ProjectionValidator.check_projections_movie(())

    def test_projections_for_movie(self):
        ProjectionValidator.check_projections_movie((1, ))

    def test_id_wrong_type(self):
        with self.assertRaises(InvalidIdTypeError):
            ProjectionValidator.check_valid_id('a')

    def test_id_wrong_negative(self):
        with self.assertRaises(InvalidIdTypeError):
            ProjectionValidator.check_valid_id('-5')

    def test_id_right_type(self):
        ProjectionValidator.check_valid_id('5')

    def test_movie_not_in_database(self):
        with self.assertRaises(MovieNotInDbError):
            ProjectionValidator.check_movie_in_db(())

    def test_movie_in_database(self):
        ProjectionValidator.check_movie_in_db((1, 'Home alone', 7.5))

    def test_seats_more_than_tickets(self):
        with self.assertRaises(WantedSeatsMoreThanTicketsError):
            ProjectionValidator.check_if_seats_more_than_tickets(100, 97)

    def test_seats_not_more_than_tickets(self):
        ProjectionValidator.check_if_seats_more_than_tickets(2, 97)

    def test_projection_id_not_for_movie_empty_tuple(self):
        with self.assertRaises(ProjectionIdNotInMovieProjectionsError):
            ProjectionValidator.check_if_projection_id_belongs_to_movie(1, ())

    def test_projection_id_not_for_movie_non_empty_tuple(self):
        with self.assertRaises(ProjectionIdNotInMovieProjectionsError):
            (ProjectionValidator
             .check_if_projection_id_belongs_to_movie(1, (4, 5, 6)))

    def test_projection_id_for_movie_non_empty_tuple(self):
        (ProjectionValidator
         .check_if_projection_id_belongs_to_movie(1, (1, 5, 6)))

    def test_reservation_id_not_for_user_empty_tuple(self):
        with self.assertRaises(ReservationIdNotInUserReservationsError):
            ProjectionValidator.check_if_reservation_id_belongs_to_user(1, ())

    def test_reservation_id_not_for_user_non_empty_tuple(self):
        with self.assertRaises(ReservationIdNotInUserReservationsError):
            (ProjectionValidator
             .check_if_reservation_id_belongs_to_user(1, (4, 5, 6)))

    def test_reservation_id_for_user_non_empty_tuple(self):
        (ProjectionValidator
         .check_if_reservation_id_belongs_to_user(1, (1, 5, 6)))


if __name__ == "__main__":
    unittest.main()
