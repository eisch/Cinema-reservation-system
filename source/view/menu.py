from controllers.main_controller import Controller
# from dateutil.parser import parse - за конвертиране на датата
from view.reservation_menu import ReservationMenu


class MainMenu:
    @classmethod
    def main_menu(cls):
        print("Welcome to our cinema reservation system!")
        print("Please choose an option. Enter 'help' for more info")
        while True:
            command = input(">>> ")
            if command.lower() == 'show movies':
                ReservationMenu.show_all_movies()
            elif command.lower().startswith('show movie projections'):
                cls.show_movie_projection_menu(command)
            elif command.lower() == 'make reservation':
                # cls.check_if_user_is_logged()
                ReservationMenu.main_reservation_menu()
            elif command.lower().startswith('cancel reservation'):
                ReservationMenu.cancel_reservation(command)
            elif command.lower() == 'exit':
                break
            elif command.lower() == 'help':
                cls.show_help()
            else:
                print("Invalid command, please try again")

    @classmethod
    def show_all_projections(cls, *args):
        movie_name = Controller.show_movie_name_by_id(args[0])[0]
        if len(args) == 1:
            print(f"Projections for movie {movie_name}")
            for projection in Controller.show_projections_by_id(args[0]):
                print(projection)
        elif len(args) == 2:
            print(f"Projections for movie {movie_name} on date {args[1]}")
            for projection in (Controller
                               .show_projections_by_id_and_date(args[0],
                                                                args[1])):
                print(projection)

    @classmethod
    def show_movie_projection_menu(cls, command):
        command_list = command.split()
        try:
            if len(command_list) == 4:
                cls.show_all_projections(command_list[3])
            elif len(command_list) == 5:
                cls.show_all_projections(command_list[3],
                                         command_list[4])
        except ValueError:
            print("Invalid values!")
        except IndexError:
            print("Too many/much arguments!")

    @classmethod
    def show_help(cls):
        print("show movies - outputs a list with all movies\n\
              show movie projection <movie_id> - outputs a list of all projections for this movie\n\
              show movie projection <movie_id> <date> - outputs a list of all projections for this movie and this date\n\
              *the date is in format 'yyyy-mm-dd'!\n\
              make reservation - gives an opportunity for making a reservation\n\
              cancel reservation - gives an opportunity for cancel a reservation\n\
              exit - exit the application")
