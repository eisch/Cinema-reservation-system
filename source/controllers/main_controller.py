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
