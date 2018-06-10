from model.models import Reservations
from controllers.session import session
from model.projection_map import ProjectionMap
from .decorators import log_info
from .validator import ProjectionValidator
from .exceptions import (InvalidIdTypeError,
                         MovieNotInDbError,
                         ProjectionsMissingMovieError,
                         WantedSeatsMoreThanTicketsError,
                         ProjectionIdNotInMovieProjectionsError,
                         ReservationIdNotInUserReservationsError)
from .movie_controller import MovieController
from .projection_controller import ProjectionController


class ReservationController:
    main_projection = ProjectionMap()

    @classmethod
    def show_seats_for_projection(cls, p_id):
        result = (session.query(Reservations.projections_id)
                  .filter(Reservations.projections_id == p_id).count())
        return 100 - result

    @classmethod
    def show_seats(cls, m_id, number_seats):
        for projection in (ProjectionController
                           .show_all_projections_by_id(m_id)):
            p_id = projection.id
            p_seats = cls.show_seats_for_projection(p_id)
            (ProjectionValidator
             .check_if_seats_more_than_tickets(number_seats, p_seats))
            print(f"{projection} - {p_seats} spots available")

    @classmethod
    def show_if_seat_is_reserved(cls, projection_id, row, column):
        result = (session.query(Reservations.id)
                  .filter(Reservations.row == row,
                          Reservations.col == column,
                          Reservations.projections_id ==
                          projection_id).first())
        return result

    @classmethod
    def reserve_seat(cls, user_id, projection_id, row, column):
        reserved_seat = Reservations(user_id=user_id,
                                     projections_id=projection_id,
                                     row=row,
                                     col=column)
        return reserved_seat

    @classmethod
    def add_all_reserved_seats(cls, reserved_seats):
        session.add_all(reserved_seats)
        session.commit()

    @classmethod
    def show_projection_map(cls, projection_id):
        cls.reserve_seat_in_the_map(projection_id)
        cls.main_projection.print_hall()

    @classmethod
    def reserve_seat_in_the_map(cls, projection_id):
        all_reserved_seats = (session.query(Reservations.row,
                                            Reservations.col)
                              .filter(Reservations.projections_id ==
                                      projection_id)
                              .all())
        for row, col in all_reserved_seats:
            cls.main_projection.reserve_seat(row, col)

    @classmethod
    def print_all_seats(cls, list_seats):
        final_result = f"Seats: "
        for item in list_seats:
            final_result += str(item)
        return final_result + '\n'

    @classmethod
    def step_one(cls):
        print("You can always stop your reservation by typing 'give up'")
        print("Step 1 (User):")
        number_seats = int(input("Choose number of tickets: "))
        MovieController.show_all_movies()
        return number_seats

    @classmethod
    def step_two(cls, number_seats):
        print("Step 2 (Movie):")
        action = input("Choose a movie: ")
        ProjectionValidator.check_valid_id(action)
        (ProjectionValidator
         .check_movie_in_db(ProjectionController
                            .show_all_projections_by_id(action)))
        cls.show_seats(action, number_seats)
        return action

    @classmethod
    def step_three(cls, movie_id):
        print("Step 3 (Projection):")
        projection = input("Choose a projection: ")
        ProjectionValidator.check_valid_id(projection)
        (ProjectionValidator
         .check_if_projection_id_belongs_to_movie
         (int(projection),
          ProjectionController.show_all_projection_ids_by_movie_id(movie_id)))
        print("Available seats (marked with a dot):")
        cls.show_projection_map(projection)
        return projection

    @staticmethod
    def seat_parser(string_seat):
        string_seat_list = string_seat.split(',')
        first = string_seat_list[0][1:]
        second = string_seat_list[1][:len(string_seat_list) - 1]
        return (int(first), int(second))

    @staticmethod
    def row_and_col_in_range(row, column):
        return row in range(1, 11) and column in range(1, 11)

    @classmethod
    def step_four(cls, number_seats, projection, current_id):
        counter, all_reserved_seats, all_row_cols = 0, [], []
        print("Choose the seat/s you want in format (number,number).")
        while counter < number_seats:
            seat = input(f"Step 4 (Seats): Choose seat {counter + 1}: ")
            row, column = cls.seat_parser(seat)
            if cls.show_if_seat_is_reserved(projection, row, column):
                print("This seat is already taken!")
            elif not cls.row_and_col_in_range(row, column):
                print("Lol...NO!")
            else:
                ru = cls.reserve_seat(current_id, projection, row, column)
                all_reserved_seats.append(ru)
                counter += 1
                all_row_cols.append((row, column))
        cls.add_all_reserved_seats(all_reserved_seats)
        print("This is your reservation.")
        print(cls.summary(projection, all_row_cols))
        return cls.summary(projection, all_row_cols)

    @classmethod
    def summary(cls, projection, list_seats):
        projection_info = (ProjectionController
                           .show_movie_date_time_projection(projection))
        seats = cls.print_all_seats(list_seats)
        return f"{projection_info}\n{seats}"

    @classmethod
    def step_five(cls, current_username, string):
            final = input("Step 5 (Confirm - type 'finalize'): ")
            if final.lower() == "finalize":
                cls.finalize(current_username, string)

    @classmethod
    @log_info
    def finalize(cls, username, string):
        print("Thanks")

    @classmethod
    def main_reservation(cls, current_id, current_username):
        try:
            print(f"Welcome, {current_username}!")
            number_seats = cls.step_one()
            movie_id = cls.step_two(number_seats)
            projection = cls.step_three(movie_id)
            summary = cls.step_four(number_seats, projection, current_id)
            cls.step_five(current_username, summary)
        except InvalidIdTypeError:
            print("Invalid id type!")
        except MovieNotInDbError:
            print("There's no movie with this id!")
        except ProjectionsMissingMovieError:
            print("There's no projection with this movie_id")
        except WantedSeatsMoreThanTicketsError:
            print("Wanted seats more than free tickets!")
        except ProjectionIdNotInMovieProjectionsError:
            print("This projection id isn't for this movie")
        except (IndexError, ValueError):
            print("Invalid value")

    @classmethod
    def list_all_reservations_by_id(cls, user_id):
        result = (session.query(Reservations)
                  .filter(Reservations.user_id == user_id).all())
        for item in result:
            print(f"{item.id} {item}")

    @classmethod
    def list_all_reservation_ids_by_id(cls, user_id):
        result = (session.query(Reservations.id)
                  .filter(Reservations.user_id == user_id).all())
        return [item[0] for item in result]

    @classmethod
    def cancel_reservation(cls, current_id):
        try:
            print("List of all your reservations: ")
            cls.list_all_reservations_by_id(current_id)
            r_id = int(input("Enter reservation id: "))
            (ProjectionValidator
             .check_if_reservation_id_belongs_to_user
             (r_id, cls.list_all_reservation_ids_by_id(current_id)))
            answer = input("Are you sure you want cancel your reservation? ")
            if answer.lower() == 'yes' or answer.lower() == 'y':
                (session.query(Reservations)
                 .filter(Reservations.id == r_id).delete())
                session.commit()
                print("You cancel your reservation successfully.")
            if answer.lower() == 'no' or answer.lower() == 'n':
                print("Okay")
        except ValueError:
            print("Invalid value type.")
        except ReservationIdNotInUserReservationsError:
            print("There's no reservation with this id for this user.")
