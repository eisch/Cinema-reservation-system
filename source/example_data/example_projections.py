from controllers.session import session
from model.models import Projections


def add_projections():
    session.add_all([Projections(movie_id=5,
                                 type="3D",
                                 date="2018-05-25",
                                 time="21:55:00"),
                     Projections(movie_id=5,
                                 type="4DX",
                                 date="2018-05-27",
                                 time="21:55:00"),
                     Projections(movie_id=4,
                                 type="2D",
                                 date="2018-05-26",
                                 time="15:30:00"),
                     Projections(movie_id=5,
                                 type="3D",
                                 date="2018-05-25",
                                 time="21:30:00")])
    session.commit()
