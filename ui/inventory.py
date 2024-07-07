import psycopg2
# from database_settings import db_params
from .display_table import print_table
import db_functions
from classes.library import Library
from classes.customers import Customers

def get_inventory():
    table_headers = ['TITLE', 'AUTHORS', 'GENRE', 'BOOK-LANGUAGE', 'PAGE-COUNT', 'SELLING-PRICE', 'STOCK']

    #try:
    connection = psycopg2.connect(**db_params)

    cursor = connection.cursor()

    table_name_books = 'books'
    table_name_customers = 'customers'

    query = f"SELECT title, authors, genre, language, page_count, selling_price, amount_total  FROM {table_name_books}"

    cursor.execute(query)

    rows = cursor.fetchall()

    print_table(table_headers, rows)

    library_json = db_functions.get_table_as_json_array(table_name_books)
    library = Library.from_dict(library_json)

    customers_json = db_functions.get_table_as_json_array(table_name_customers)
    customers = Customers.from_dict(customers_json)

    search_query = input("Search a book: ")
    search_results = library.search_book(search_query)

    if search_results:
        print("Search Results")
        print("--------------")
        for id, book in enumerate(search_results):
            print(f"[{id+1}] | {book}")

    else:
        print("Not search results available! Redirecting back to menu...")
        return
    
    choice = input("\nIn order to choose a book, enter a book id, or type 'x' to quit to menu: ")
    if (choice == 'x'):
        return
    
    ##add error handling here
    book = search_results[int(choice)-1]

    choice = input("Would you like to sell this book to a customer? (y/n): ")

    if (choice == 'y'):
        customer_id = int(input("Please provide a customer id: "))
        customer = customers.search_customer_by_id(customer_id)

        if customer:
            choice = input(f"Customer: {customer}, price: {book.get_price()} confirm? (y/n): ")

            if (choice == 'y'):        
                                
                #sell book from library
                #add book to customer books list
                #update to database customers_list

                library.sell_to_customer(customer,book)
                customer.purchase(book)
                db_functions.update_customer_purchase_list(customer)


            



        

        

# except (Exception, psycopg2.DatabaseError) as error:
#     print(f"Error: {error}")
