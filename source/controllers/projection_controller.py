from model.models import Projections
from controllers.session import session
from controllers.validator import ProjectionValidator


class ProjectionController:
    @classmethod
    def show_all_projectons_by_id(cls, movie_id):
        result = (session.query(Projections).filter
                  (Projections.movie_id == movie_id).all())
        return result

    @classmethod
    def show_all_projections_by_id_and_date(cls,
                                            projection_id,
                                            projection_date):
        result = (session.query(Projections).filter
                  (Projections.id == projection_id,
                   Projections.date == projection_date).all())
        return result

    @classmethod
    def show_movie_date_time_projection(cls, pr_id):
        result = (session.query(Projections)
                  .filter(Projections.id == pr_id).first())
        new_str_movie = f"Movie: {''.join(str(result.movie).split(' - ')[1:])}"
        new_result = f"Date and time: {''.join(str(result).split(' - ')[1:])}"
        print(new_str_movie)
        print(new_result)
        return f"{new_str_movie}\n{new_result}"
