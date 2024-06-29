import api_functions
import db_functions
import classes.library as library
from classes.book import Book

 


def search_books():  


    amount_of_search_results = 10   
    print('\n(1) Search books')  
    query = input("\t- search for a book by title: ")
    search_results = api_functions.search_books(query , amount_of_search_results)  

    print(f'\t\t-- Top {amount_of_search_results} books matching your search results: ')
    print(f'\t\tID | TITLE')
    for id,book in enumerate(search_results):
        print(f'\t\t[{id + 1}]| {book['title']}')

    
    try:
        book_id = int(input('\t\t-- To add a book to the inventory, enter the id: '))
        if book_id not in range(1,11):
            raise ValueError
        else:
            book_json = search_results[book_id-1]
            book_obj = Book.from_dict(book_json)
        
    except ValueError:
        print('Invalid Input! A number between 1-10 must be provided. Try again...')
        search_books()
    
    amount_of_books = input('\t\t-- How many copies do you want to add to the inventory?: ')

    try:
        amount_of_books = int(amount_of_books)

    except ValueError:
        print('\t\tInvalid Input! A number must be provided. Try again...')
        search_books()

    to_add = input(f'\t\tConfirm adding {amount_of_books} copies of {book_obj.get_title()} to inventory (y/n): ') 
    if to_add == 'y':
        inventory_json = db_functions.get_table_as_json_array(table_name = 'books') 
        inventory = library.Library.from_dict(inventory_json)
        inventory.add_book(book_obj,amount_of_books)
        print('\n\t\t Book was added successfully!\n')
        print(inventory)
        db_functions.add_book_to_books_table(book_json)