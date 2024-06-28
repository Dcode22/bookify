import psycopg2
from database_settings import db_params

def manage_customers():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    print('''
          CUSTOMER MANAGEMENT
          -------------------
          '''
    )
    choice = input(
        '''
        (l) List all customers
        (s) Search for customer by name
        (n) Create new customer
        (b) Go back to main menu
        Enter an option:
        '''
    )

    if choice == 'l':
        list_all_customers(cur, conn)
    elif choice == 's':
        search_customers()
    elif choice == 'n':
        new_customer()
    elif choice == 'b':
        print('going back to main menu')
        return 
    else:
        print("Invalid option")
        manage_customers()



def list_all_customers(cur, conn):
    query = "SELECT * FROM customers"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def search_customers():
    return 

def new_customer(cur, conn):

    query = "INSERT INTO customers ()"

    return 
#     (l) list all customers
#         ------|-----------------|---------------
#         id    | name            | address
#         ------|-----------------|---------------
#         id    | name            | address
#         ------|-----------------|---------------
#         id    | name            | address
#         ------|-----------------|---------------



#     (s) search for customer by name
#         matches:
#         ------|-----------------|---------------
#         id    | name            | address
#         ------|-----------------|---------------
#         id    | name            | address
#         ------|-----------------|---------------
#         id    | name            | address
#         ------|-----------------|---------------

#         -- select user by id: 
        
#         -- 
#         USER NAME
#         select an option:
#             (d) delete user
#             (u) update user
#                 1. update name
#                 2. update address
#                 ...
#                 -- select option to update:
#                 --enter new value
#                 -- Confirm
#                 --success/failure
    
#     (n) create new customer
#         -- input name
#         -- input email
#         ....
#         -- confirm (display info):
#         -- success/failure

#     (b) go back
