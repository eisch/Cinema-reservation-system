from controllers.session import session
from model.models import Movies


def add_movies():
    session.add_all([
                    Movies(name="The Hunger Games: Catching Fire", rating=7.5),
                    Movies(name="Wreck-It Ralph", rating=7.8),
                    Movies(name="Her", rating=8.3),
                    Movies(name="Avengers: Infinity War", rating=8.8)])

    session.commit()


