import api_functions
from ui.search_books import search_books

menu_msg = ''' 
        Menu :
        (1) Search books
        (2) Open inventory
        (3) Manage customers 
        (x) Exit
        Choose an option >> '''

def display_menu():
    choice = input(menu_msg)
    if choice == '1':
        search_books()
    elif choice == '2':
        return
    elif choice == '3':
        return
    elif choice == 'x':
        return
    else:
        print('invalid choice')
        display_menu()
    
    


def main():
    welcome_msg = '''
    ------------Welcome to Bookify!------------
    ---The World's #1 Book Management System---'''
    print(welcome_msg)
    while True:
        display_menu()

if __name__ == '__main__':
    main()