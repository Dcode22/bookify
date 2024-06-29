from .manage_customers import manage_customers
from .inventory import get_inventory
from .search_books import search_books

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
        get_inventory()
        return
    elif choice == '3':
        manage_customers()
        return
    elif choice == 'x':
        return
    else:
        print('invalid choice')
        display_menu()
    
    
