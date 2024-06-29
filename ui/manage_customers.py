import psycopg2
from database_settings import db_params
from .display_table import print_table
def manage_customers():
    print('''
CUSTOMER MANAGEMENT
-------------------
'''
    )
    choice = input(
        '''
(l) List all customers
(s) Search for customer
(n) Create new customer
(b) Go back to main menu
Enter an option:
'''
    )

    if choice == 'l':
        list_all_customers()
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



def list_all_customers():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    query = "SELECT * FROM customers"
    cur.execute(query)
    rows = cur.fetchall()
    table_headers = ["CUSTOMER ID", "FIRST NAME", "LAST NAME", "EMAIL", "PHONE"]
    print_table(table_headers, rows)
    cur.close()
    conn.close()
    manage_customers()

def search_customers():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    search = input("Search customers: ")
    query = f"SELECT * FROM customers WHERE LOWER(CONCAT(first_name, ' ', last_name, ' ', email)) LIKE LOWER('%{search}%');"
    cur.execute(query)
    rows = cur.fetchall()
    table_headers = ["CUSTOMER ID", "FIRST NAME", "LAST NAME", "EMAIL", "PHONE"]
    print_table(table_headers, rows)
    cur.close()
    conn.close()

    customer_id = int(input("Select a customer by ID:"))
    customer = [customer for customer in rows if customer[0] == customer_id][0]
    if customer:
        print(f"{customer[1]} {customer[2]}".upper())
        choice = input('''
select an option:
(d) delete user
(u) update user
''')
        if choice == 'd':
            confirmation = input(f'To confirm that you want to permanently delete the customer {customer[1]} {customer[2]}, type yes, otherwise type x:')
            if confirmation == 'yes':
                conn = psycopg2.connect(**db_params)
                cur = conn.cursor()
                query = "DELETE FROM customers WHERE customer_id = %s;"
                cur.execute(query, (customer[0], ))
                conn.commit()
                print(cur.statusmessage)
                cur.close()
                conn.close()
                manage_customers()
            else:
                manage_customers()
        elif choice == 'u':
            choice = input('''
(1) Update first name
(2) Update last name
(3) Update email address
(4) Update phone number
''')
            choices = ['first_name', 'last_name', 'email', 'phone']
            new_value = ''
            if choice == '1':
                new_value = input(f'Enter new first name for {customer[1]} {customer[2]}: ')
            elif choice == '2':
                new_value = input(f'Enter new last name for {customer[1]} {customer[2]}: ')
            elif choice == '3':
                new_value = input(f'Enter new email for {customer[1]} {customer[2]}: ')
            elif choice == '4':
                new_value = input(f'Enter new phone number for {customer[1]} {customer[2]}: ')
            else:
                print('Invalid option')
                search_customers()
            confirmation = input(f"Are you sure you want to update the {choices[int(choice)-1]} for {customer[1]} {customer[2]} to {new_value}? (y/n)")
            if confirmation == 'y':
                conn = psycopg2.connect(**db_params)
                cur = conn.cursor()
                query = f"UPDATE customers SET {choices[int(choice)-1]} = %s WHERE customer_id = {customer[0]};"
                cur.execute(query, (new_value, ))
                conn.commit()
                print(cur.statusmessage)
                cur.close()
                conn.close()
                search_customers()

def new_customer():
    print("CREATE NEW CUSTOMER")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    print(f"FIRST NAME: {first_name}, LAST NAME: {last_name}, EMAIL: {email}, PHONE: {phone}")
    confirmation = input("Are you sure you want to create this customer? (y/n)")
    if confirmation == 'y':
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        query = "INSERT INTO customers (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (first_name, last_name, email, phone))
        conn.commit()
        print(cur.statusmessage)
        cur.close()
        conn.close()
        manage_customers()
    else:
        manage_customers()
