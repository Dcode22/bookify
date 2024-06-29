import psycopg2
import psycopg2.sql
from database_settings import db_params

def create_connection():
    connection = psycopg2.connect(**db_params)
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
    book_id_field = 'book_id'
    amount_available_field = 'amount_available'
    amount_total_field = 'amount_total'
    connection, cursor = create_connection()

    #get the current amount_available value of the book
    select_query = f"SELECT {amount_available_field} FROM {table_name} WHERE {book_id_field} = %s"
    cursor.execute(select_query,(book_data['book_id'],))
    rows = (cursor.fetchall())

    if rows: #if book exists in table
        #calculate amount_available:
        old_amount_available = rows[0][0]
        new_amount_available = old_amount_available + book_data['amount_available']

        #calculate amount_total:
        select_query = f"SELECT {amount_total_field} FROM {table_name} WHERE {book_id_field} = %s"
        cursor.execute(select_query,(book_data['book_id'],))
        rows = (cursor.fetchall())
        old_amount_total = rows[0][0]
        new_amount_total = old_amount_total + book_data['amount_total']

        #update new values in table
        update_query = f"UPDATE {table_name} SET {amount_available_field} = %s, {amount_total_field} = %s WHERE {book_id_field} = %s"
        cursor.execute(update_query,(new_amount_available,new_amount_total,book_data['book_id']))
        connection.commit()
        
    else:
        #if book doesn't exist in table, add a new book
        insert_query = psycopg2.sql.SQL(f"""
        INSERT INTO {table_name} (
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