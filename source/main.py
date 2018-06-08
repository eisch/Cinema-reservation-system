from model.models import CreateDatabase
from view.menu import MainMenu
from example_data import example_movies, example_projections, example_reservations


def main():
    # CreateDatabase.create_db()
    MainMenu.main_menu()
    # example_movies.add_movies()
    # example_projections.add_projections()
    # example_reservations.create_reservations()


if __name__ == "__main__":
    main()
