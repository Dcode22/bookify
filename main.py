import api_functions
from ui.menu import display_menu


def main():
    welcome_msg = '''
------------Welcome to Bookify!------------
---The World's #1 Book Management System---'''
    print(welcome_msg)
    while True:
        display_menu()

if __name__ == '__main__':
    main()