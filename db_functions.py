import psycopg2
import psycopg2.sql

HOST = "localhost"
PORT = "5432"
USER = "postgres"
PASSWORD = "cluster"
DBNAME = "bookify"

def create_connection():
    connection = psycopg2.connect(
        host=HOST, port=PORT, user=USER, password=PASSWORD, dbname=DBNAME
    )
    cursor = connection.cursor()
    return connection, cursor



def get_table_as_json_array(table_name : str) -> list[dict]:
    connection, cursor = create_connection()

    try:
        #Get data from the table as JSON array
        query = f"SELECT json_agg(row_to_json({table_name})) FROM {table_name};"

        cursor.execute(query)

        json_result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return json_result
    
    except Exception as e:
        print(f"Error fetching data from {table_name}. Error: {e}")
        return None
    


def add_book_to_books_table(book_data:dict) -> None:
    table_name = 'books'
    connection, cursor = create_connection()

    insert_query = psycopg2.sql.SQL("""
    INSERT INTO books (
        book_id, title, description, authors, genre, published_date, language, 
        page_count, cover_image_url, publisher, avg_rating, maturity_rate, 
        buying_price, selling_price, amount_total, amount_available
    ) VALUES (
        %(book_id)s, %(title)s, %(description)s, %(authors)s, %(genre)s, %(published_date)s, %(language)s, 
        %(page_count)s, %(cover_image_url)s, %(publisher)s, %(avg_rating)s, %(maturity_rate)s, 
        %(buying_price)s, %(selling_price)s, %(amount_total)s, %(amount_available)s
    )
""")
    
    cursor.execute(insert_query,book_data)
    connection.commit()
    cursor.close()
    connection.close()