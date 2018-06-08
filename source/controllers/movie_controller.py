from model.models import Movies
from controllers.session import session
from controllers.validator import MovieValidator
from controllers.exceptions import (MovieAlreadyInDatabaseError,
                                    RatingNotInRangeError)


class MovieController:
    @classmethod
    def create(cls, m_name, m_rating):
        try:
            m_rating = float(m_rating)
            MovieValidator.check_all(m_name, m_rating)
            movie = Movies(name=m_name, rating=m_rating)
            cls.check_if_movie_is_in_db_already(m_name, m_rating)
            session.add(movie)
            session.commit()
        except ValueError:
            print("Invalid rating or movie's name format!")
        except RatingNotInRangeError:
            print("The rating must be between 1 and 10!")
        except MovieAlreadyInDatabaseError:
            print("The movie is already in database!")

    @classmethod
    def check_if_movie_is_in_db_already(cls, m_name, m_rating):
        result = session.query(Movies).filter(Movies.name == m_name,
                                              Movies.rating == m_rating).all()
        if len(result) != 0:
            raise MovieAlreadyInDatabaseError()

    @classmethod
    def show_all_movies(cls):
        result = session.query(Movies).all()
        return result

    @classmethod
    def show_movie_name_by_id(cls, m_id):
        result = session.query(Movies.name).filter(Movies.id == m_id).one()
        return result




