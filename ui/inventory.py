import psycopg2
from database_settings import db_params

def get_inventory():
    table_headers = ['ID', 'TITLE', 'AUTHORS', 'PUBLISHER', 'PUBLISHER-DATE', 'DESCRIPTION', 'PAGE-COUNT', 'GENRE', 'AVERAGE-RATING', 'MATURITY-RATING', 'SMALL-THUMBNAIL', 'LANGUAGE', 'PRICE', 'BOOK-LANGUAGE', 'STOCK']

    try:
        connection = psycopg2.connect(**db_params)

        cursor = connection.cursor()

        query = "SELECT * FROM books"

        cursor.execute(query)

        rows = cursor.fetchall()

        col_widths = [len(header) for header in table_headers]
        
        for row in rows:
            for i, field in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(field)))
        
        header_row = ' | '.join(header.ljust(col_widths[i]) for i, header in enumerate(table_headers))
        separator_row = '-+-'.join('-' * col_widths[i] for i in range(len(table_headers)))

        print("This is your books inventory: ->")
        print(separator_row)
        print(header_row)
        print(separator_row)

        for row in rows:
            data_row = ' | '.join(str(field).ljust(col_widths[i]) for i, field in enumerate(row))
            print(data_row)
            print(separator_row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")











