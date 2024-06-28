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
        print('you picked 1')
    elif choice == '2':
        return
    elif choice == '3':
        return
    elif choice == 'x':
        return
    else:
        print('invalid choice')
        display_menu()
    
    
