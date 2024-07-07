import psycopg2
# from database_settings import db_params
from .display_table import print_table
def manage_customers():
    print('''
+---------------------+
| CUSTOMER MANAGEMENT |
+---------------------+'''
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
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        query = "SELECT * FROM customers"
        cur.execute(query)
        rows = cur.fetchall()
        table_headers = ["CUSTOMER ID", "FIRST NAME", "LAST NAME", "EMAIL", "PHONE", "PURCHASES"]
        print_table(table_headers, rows)
        cur.close()
        conn.close()
        manage_customers()
    except Exception as e:
        print('Error: ', e)

def search_customers():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        search = input("SEARCH CUSTOMERS (type 'x' to cancel): ")
        if search == 'x':
            return manage_customers()
        query = f"SELECT * FROM customers WHERE LOWER(CONCAT(first_name, ' ', last_name, ' ', email)) LIKE LOWER('%{search}%');"
        cur.execute(query)
        rows = cur.fetchall()
        table_headers = ["CUSTOMER ID", "FIRST NAME", "LAST NAME", "EMAIL", "PHONE", "PURCHASES"]
        print_table(table_headers, rows)
        cur.close()
        conn.close()
        if len(rows) == 0:
            print('NO CUSTOMERS MATCHED YOUR SEARCH')
            return search_customers()

        select_customer_by_id(rows)
    except Exception as e:
        print('Error:', e)
        print('Try again')
        search_customers()


def select_customer_by_id(rows):
    global updated_customer_obj
    customer_id = int(input("Select a customer by ID:"))
    matching_customers = [customer for customer in rows if customer[0] == customer_id]
    if len(matching_customers):
        customer = matching_customers[0]
        updated_customer_obj = {
            'first_name': customer[1],
            'last_name': customer[2],
            'email': customer[3],
            'phone': customer[4]
        }
        choice = input(f'''
CUSTOMER: {f"{customer[1]} {customer[2]}".upper()}
select an option:
(d) delete customer
(u) update customer
(x) cancel

    ''')

        if choice == 'd':
            delete_customer(customer)
        elif choice == 'u':
            update_customer(customer)
        elif choice == 'x':
            search_customers()
    else:
        print('INVALID SELECTION, TRY AGAIN')
        select_customer_by_id(rows)



def delete_customer(customer):
    try: 
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
    except Exception as e:
        print('Error:', e)
        search_customers()

updated_customer_obj = {}

def update_customer(customer):
    print('update customer func')
    print(f'''
          

CUSTOMER
---------------
FIRST NAME: {updated_customer_obj["first_name"]} 
LAST NAME: {updated_customer_obj["last_name"]} 
EMAIL: {updated_customer_obj["email"]} 
PHONE: {updated_customer_obj["phone"]}''')
    choice = input('''
(1) Update first name
(2) Update last name
(3) Update email address
(4) Update phone number
(x) Cancel

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
    elif choice == 'x':
        manage_customers()
    else:
        print('Invalid option')
        search_customers()
    confirmation = input(f"Are you sure you want to update the {choices[int(choice)-1]} for {customer[1]} {customer[2]} to {new_value}? (y/n)")
    if confirmation == 'y':
        try:
            conn = psycopg2.connect(**db_params)
            cur = conn.cursor()
            query = f"UPDATE customers SET {choices[int(choice)-1]} = %s WHERE customer_id = {customer[0]};"
            cur.execute(query, (new_value, ))
            conn.commit()
            print(cur.statusmessage)
            cur.close()
            conn.close()
            updated_customer_obj[choices[int(choice)-1]] = new_value
            update_customer(customer)
        except Exception as e:
            print('Error:', e)
            print('Try again')
            update_customer(customer)



def new_customer():
    print('''
CREATE NEW CUSTOMER
-------------------

''')
    first_name = input("Enter first name (enter 'x' to cancel): ")
    if first_name == 'x':
        manage_customers()
    last_name = input("Enter last name (enter 'x' to cancel): ")
    if last_name == 'x':
        manage_customers()
    email = input("Enter email (enter 'x' to cancel): ")
    if email == 'x':
        manage_customers()
    phone = input("Enter phone (enter 'x' to cancel): ")
    if phone == 'x':
        manage_customers()
    print(f"FIRST NAME: {first_name}, LAST NAME: {last_name}, EMAIL: {email}, PHONE: {phone}")
    
    confirmation = input("Are you sure you want to create this customer? (y/n)")
    
    if confirmation == 'y':
        try:
            conn = psycopg2.connect(**db_params)
            cur = conn.cursor()
            query = "INSERT INTO customers (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (first_name, last_name, email, phone))
            conn.commit()
            print(cur.statusmessage)
            cur.close()
            conn.close()
            manage_customers()
        except Exception as e:
            print('Error creating user:', e)
            print('Try again')
            new_customer()
    else:
        manage_customers()
