from controllers.session import session
from model.models import Reservations


def create_reservations():
    session.add_all([Reservations(user_id=1, projections_id=2, row=2, col=4),
                     Reservations(user_id=1, projections_id=2, row=2, col=3)])
    session.commit()
