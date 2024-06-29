import psycopg2
from database_settings import db_params
from .display_table import print_table
def get_inventory():
    table_headers = ['TITLE', 'AUTHORS', 'GENRE', 'BOOK-LANGUAGE', 'PAGE-COUNT', 'SELLING-PRICE', 'STOCK']

    try:
        connection = psycopg2.connect(**db_params)

        cursor = connection.cursor()

        query = "SELECT title, authors, genre, language, page_count, selling_price, amount_total  FROM books"

        cursor.execute(query)

        rows = cursor.fetchall()

        print_table(table_headers, rows)

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
