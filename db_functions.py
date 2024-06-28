import psycopg2
import json

HOST = "localhost"
PORT = "5432"
USER = "postgres"
PASSWORD = "cluster"
DBNAME = "bookify"

def create_connection():
    connection = psycopg2.connnect(
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