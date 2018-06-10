from controllers.movie_controller import MovieController
from controllers.projection_controller import ProjectionController
from controllers.reservations_controller import ReservationController
from controllers.user_controller import UserController


class Controller:
    @classmethod
    def show_all_movies(cls):
        return MovieController.show_all_movies()

    @classmethod
    def show_projections(cls, *args):
        return ProjectionController.show_projections(*args)

    @classmethod
    def register_user(cls, username, password):
        return UserController.register(username, password)

    @classmethod
    def user_id_by_username(cls, username):
        return UserController.user_id_by_username(username)

    @classmethod
    def make_reservation(cls, current_id, current_username):
        return (ReservationController
                .main_reservation(current_id, current_username))

    @classmethod
    def cancel_reservation(cls, r_id):
        return ReservationController.cancel_reservation(r_id)
    # @classmethod
    # def show_seats_by_projection_id(cls, p_id):
    #     return ReservationController.show_seats(p_id)



    # @classmethod
    # def show_hall(cls, projection_id):
    #     return ReservationController.show_projection_map(projection_id)

    # @classmethod
    # def reserve_seat(cls, user_id, projection_id, row, column):
    #     return (ReservationController
    #             .reserve_seat(user_id,
    #                           projection_id,
    #                           row,
    #                           column))

    # @classmethod
    # def add_all_reserved_seats(cls, list_reserved_seats):
    #     return (ReservationController
    #             .add_all_reserved_seats(list_reserved_seats))

    # @classmethod
    # def show_movie_date_time_projection(cls, pr_id):
    #     return ProjectionController.show_movie_date_time_projection(pr_id)

    # @classmethod
    # def summary_reservation(cls, user_id, p_id):
    #     time_projection = (ProjectionController
    #                        .show_movie_date_time_projection(p_id))
    #     all_seats = (ReservationController
    #                  .list_current_seats_reservation(user_id, p_id))
    #     return f"{time_projection} {all_seats}"

    # @classmethod
    # def finalize(cls, username, user_id, p_id):
    #     a = cls.summary_reservation(user_id, p_id)
    #     return ReservationController.finalize(username, a)

    # @classmethod
    # def list_all_reservations_by_id(cls, user_id):
    #     return ReservationController.list_all_reservations_by_id(user_id)



    # @classmethod
    # def list_all_seats_reservation(cls, user_id, projection_id):
    #     return (ReservationController
    #             .list_current_seats_reservation(user_id, projection_id))



