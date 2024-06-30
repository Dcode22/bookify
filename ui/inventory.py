import psycopg2
from database_settings import db_params
from .display_table import print_table
import db_functions
from classes.library import Library
from classes.customers import Customers

def get_inventory():
    table_headers = ['TITLE', 'AUTHORS', 'GENRE', 'BOOK-LANGUAGE', 'PAGE-COUNT', 'SELLING-PRICE', 'STOCK']

    try:
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
        library = Customers.from_dict(customers_json)

        search_query = input("Search a book: ")
        search_results = library.search_book(search_query)

        if search_results:
            for id, book in enumerate(search_results):
                print(f"[{id+1}] | {book}")

        else:
            print("Not search results available! Redirecting back to menu...")
            return

        #choice = ("Would you like to sell this book to a customer? (y/n): ")

        #if choice == 'y':



        

        

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
