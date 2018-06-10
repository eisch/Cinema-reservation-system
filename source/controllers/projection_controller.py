from model.models import Projections
from controllers.session import session
from controllers.validator import ProjectionValidator
from controllers.exceptions import (ProjectionsMissingMovieError,
                                    InvalidIdTypeError)
from dateutil import parser


class ProjectionController:
    @classmethod
    def show_all_projections_by_id(cls, movie_id):
        result = (session.query(Projections).filter
                  (Projections.movie_id == movie_id).all())
        return result

    @classmethod
    def show_all_projection_ids_by_movie_id(cls, movie_id):
        result = (session.query(Projections.id).filter
                  (Projections.movie_id == movie_id).all())
        return [item[0] for item in result]

    @classmethod
    def show_all_projections_by_id_and_date(cls,
                                            movie_id,
                                            projection_date):
        result = (session.query(Projections).filter
                  (Projections.movie_id == movie_id,
                   Projections.date == projection_date).all())
        return result

    @classmethod
    def show_movie_name_by_id(cls, id_movie):
        result = (session.query(Projections)
                  .filter(Projections.movie_id == id_movie).first())
        ProjectionValidator.check_projections_movie(result)
        m_name = result.movie.name
        return m_name

    @classmethod
    def show_movie_date_time_projection(cls, pr_id):
        result = (session.query(Projections)
                  .filter(Projections.id == pr_id).first())
        new_str_movie = f"Movie: {''.join(str(result.movie).split(' - ')[1:])}"
        new_result = f"Date and time: {''.join(str(result).split(' - ')[1:])}"
        return f"{new_str_movie}\n{new_result}"

    @classmethod
    def show_projections(cls, *args):
        try:
            ProjectionValidator.check_valid_id(args[0][0])
            movie_name = cls.show_movie_name_by_id(int(args[0][0]))
            if len(*args) == 1:
                print(f"Projections for movie {movie_name}")
                for item in cls.show_all_projections_by_id(*args[0]):
                    print(item)
            elif len(*args) == 2:
                date = parser.parse(args[0][1]).date()
                print(f"Projections for movie {movie_name} on date {date}")
                for item in cls.show_all_projections_by_id_and_date(args[0][0], args[0][1]):
                    print(item)
        except ValueError:
            print("Invalid date format! Please use format <yyyy-mm-dd>")
            return False
        except ProjectionsMissingMovieError:
            print("There's no projections for this movie!")
            return False
        except InvalidIdTypeError:
            print("Invalid id type!")
            return False
