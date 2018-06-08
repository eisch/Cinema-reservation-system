from model.models import Reservations
from controllers.session import session
from model.projection_map import ProjectionMap
from .decorators import log_info


class ReservationController:
    main_projection = ProjectionMap()

    @classmethod
    def show_seats(cls, p_id):
        result = (session.query(Reservations.projections_id)
                  .filter(Reservations.projections_id == p_id).count())
        return 100 - result

    @classmethod
    def show_if_seat_is_reserved(cls, row, column):
        result = (session.query(Reservations.id)
                  .filter(Reservations.row == row,
                          Reservations.col == column).first())
        return result

    # TODO: try except !!!
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
    @log_info
    def finalize(cls, username, string):
        print("Thanks")

    @classmethod
    def cancel_reservation(cls, r_id):
        session.query(Reservations).filter_by(Reservations.id == r_id).delete()
        session.commit()

    @classmethod
    def list_all_reservations_by_id(cls, user_id):
        result = (session.query(Reservations)
                  .filter(Reservations.user_id == user_id).all())
        return result


