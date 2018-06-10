from controllers.main_controller import Controller
from view.current_logged_user import (logged_user,
                                      current_username,
                                      current_id)
from getpass import getpass


class MainMenu:
    @classmethod
    def main_menu(cls):
        print("Welcome to our cinema reservation system!")
        print("Please choose an option. Enter 'help' for more info")
        global current_username, current_id
        while True:
            command = input(">>> ")
            if command.lower() == 'show movies':
                Controller.show_all_movies()
            elif command.lower().startswith('show movie projection'):
                list_command = command.split()[3:]
                if len(list_command) < 3:
                    Controller.show_projections(list_command)
                else:
                    print("Too much arguments")
            elif command.lower() == 'make reservation':
                if cls.check_if_user_is_logged():
                    Controller.make_reservation(current_id, current_username)
            elif command.lower().startswith('cancel reservation'):
                if cls.check_if_user_is_logged():
                    Controller.cancel_reservation(current_id)
            elif command.lower() == 'exit':
                break
            elif command.lower() == 'help':
                cls.show_help()
            else:
                print("Invalid command, please try again")

    @classmethod
    def check_if_user_is_logged(cls):
        global logged_user, current_username, current_id
        if logged_user:
            return True
        else:
            print("You need to a user in the system to make reservations!")
            username = input("Username: ")
            current_username = username
            password = getpass()
            if not Controller.register_user(username, password):
                logged_user = True
                current_id = Controller.user_id_by_username(username)
                return True
            else:
                print("Registration failed.")
                return False

    @classmethod
    def show_help(cls):
        print("show movies - outputs a list with all movies\n\
              show movie projection <movie_id> - outputs a list of all projections for this movie\n\
              show movie projection <movie_id> <date> - outputs a list of all projections for this movie and this date\n\
              *the date is in format 'yyyy-mm-dd'!\n\
              make reservation - gives an opportunity for making a reservation\n\
              cancel reservation - gives an opportunity for cancel a reservation\n\
              exit - exit the application")
