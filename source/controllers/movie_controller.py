from model.models import Movies
from controllers.session import session


class MovieController:
    @classmethod
    def show_all_movies(cls):
        for item in session.query(Movies).all():
            print(item)
