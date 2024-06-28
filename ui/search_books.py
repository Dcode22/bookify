import api_functions
import db_functions
import classes.library as library

 


def search_books():  

    inventory_json = db_functions.get_table_as_json_array(table_name = 'books') 
    inventory = library.from_dict(inventory_json)

    amount_of_search_results = 10   
    print('(1) Search books')  
    query = input("\t- search for a book by title: ")
    books_results = api_functions.search_books(query , amount_of_search_results) #search_books function is needed. return here a list of book objects. randomize a price for the book object
    books_results = library.from_dict(books_results)

    print(f'\t\t-- Top {amount_of_search_results} books matching your search results: ')
    print(f'\t\t\tID | TITLE')
    for id,book in enumerate(books_results):
        print(f'[{id + 1}]| {book.title}')

    book_id = input('\t\t-- To add a book to the inventory, enter the id: ')
    
    try:
        book_id = int(book_id)
        if book_id not in range(1,11):
            raise ValueError
        else:
            selected_book = books_results[book_id-1]
        
    except ValueError:
        print('Invalid Input! A number between 1-10 must be provided. Try again...')
        search_books()
    
    amount_of_books = input('\t\t-- How many copies do you want to add to the inventory?: ')

    try:
        amount_of_books = int(amount_of_books)

    except ValueError:
        print('Invalid Input! A number must be provided. Try again...')
        search_books()

    to_add = input(f'Confirm adding {amount_of_books} copies of {selected_book.get_title()} to inventory (y/n): ') 
    if to_add == 'y':
        inventory.add_book(selected_book) # Need to implement - create new book or change stock if already exists