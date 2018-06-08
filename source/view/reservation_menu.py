from controllers.main_controller import Controller
from getpass import getpass
from view.current_logged_user import logged_user, current_username, current_id


class ReservationMenu:
    @classmethod
    def check_if_user_is_logged(cls):
        global logged_user, current_username, current_id
        if logged_user:
            cls.make_reservation_submenu()
        else:
            print("You need to a user in the system to make reservations!")
            username = input("Username: ")
            current_username = username
            password = getpass()
            Controller.register_user(username, password)
            logged_user = True
            current_id = Controller.user_id_by_username(username)
            cls.make_reservation_submenu()

    @classmethod
    def show_all_movies(cls):
        for movie in Controller.show_all_movies():
            print(movie)

    @classmethod
    def show_seats(cls, m_id):
        for projection in Controller.show_projections_by_id(m_id):
            p_id = projection.id
            p_seats = Controller.show_seats_by_projection_id(p_id)
            print(f"{projection} - {p_seats} spots available")

    @classmethod
    def make_reservation_submenu(cls):
        print("Step 1 (User):")
        number_seats = int(input("Choose number of tickets: "))
        cls.show_all_movies()
        print("Step 2 (Movie):")
        action = input("Choose a movie: ")
        cls.show_seats(action)
        print("Step 3 (Projection):")
        projection = input("Choose a projection: ")
        print("Available seats (marked with a dot):")
        Controller.show_hall(projection)
        cls.reserve_seats(number_seats, projection)
        cls.final_message(projection)
        final = input("Step 5 (Confirm - type 'finalize'): ")
        if final.lower() == "finalize":
            Controller.finalize(current_username, projection)

    @staticmethod
    def seat_parser(string_seat):
        string_seat_list = string_seat.split(',')
        first = string_seat_list[0][1:]
        second = string_seat_list[1][:len(string_seat_list) - 1]
        return (int(first), int(second))

    @classmethod
    def reserve_seats(cls, number_of_seats, projection):
        all_reserved_seats = []
        for count in range(number_of_seats):
            seat = input(f"Choose seat {count + 1}")
            row, col = cls.seat_parser(seat)
            ru = Controller.reserve_seat(current_id, projection, row, col)
            all_reserved_seats.append(ru)
        Controller.add_all_reserved_seats(all_reserved_seats)

    @classmethod
    def final_message(cls, pr_id):
        print("This is your reservation:")
        Controller.show_movie_date_time_projection(pr_id)

    @classmethod
    def main_reservation_menu(cls):
        cls.check_if_user_is_logged()

    @classmethod
    def cancel_reservation(cls, command):
        pass
        # list_answer = command.split()
        # print("List of all your reservations: ")

        # answer = input("Are you sure that you want cancel your reservation?")
        # if answer.lower() == 'yes':
        #     Controller.cancel_reservation(r_id)
        #     print("You cancel your reservation successfully")
        # if answer.lower() == 'no':
        #     print("Okay")

    @classmethod
    def list_all_reservations_by_user_id(cls, user_id):
        for item in Controller.list_all_reservations_by_id(user_id):
            print(item)
