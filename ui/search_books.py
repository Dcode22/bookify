import api_functions
import db_functions
from classes.library import Library
from classes.book import Book

 


def search_books():  

    print(
        '''
        Search books
        ------------''')
    
    query = input("\tSearch a book by title: ")
        
    search_results = api_functions.search_books(query, 10)

    if search_results:
        display_search_results(search_results)

        id = int(input("\n\tTo add a book to the inventory, enter the id (1-10): "))
        user_selected_book_json = search_results[id-1]

        amount = int(input("\tHow many copies do you want to add to the inventory?: "))
        user_selected_book_json['amount_total'] = user_selected_book_json['amount_available'] = amount

        to_add = input(f"\tConfirm adding {amount} copies of {user_selected_book_json['title']} to inventory (y/n): ")
        if (to_add == 'y'):
            db_functions.add_book_to_books_table(user_selected_book_json)
            print("\tBook was successfuly added.")



def display_search_results(search_results :list[dict]) -> None:
    print(f"\tTop {len(search_results)} books matching your results: ")
    print("\tID | TITLE")
    for id,result in enumerate(search_results):
        print(f"\t[{id+1}]| {result['title']}") #id starts with 0, so changed it to id+1

    
    # print('\n\t(1) Search books')  
    # query = input("\t- search for a book by title: ")

    # amount_of_search_results = 10   
    # search_results = api_functions.search_books(query , amount_of_search_results)  

    # print(f'\t-- Top {amount_of_search_results} books matching your search results: ')
    # print(f'\tID | TITLE')
    # for id,book in enumerate(search_results):
    #     print(f'\t[{id + 1}]| {book['title']}')


    # try:
    #     book_id = int(input('\t-- To add a book to the inventory, enter the id: '))
    #     if book_id not in range(1,11):
    #         raise ValueError
    #     else:
    #         book_json = search_results[book_id-1]
    #         book_obj = Book.from_dict(book_json)
        
    # except ValueError:
    #     print('Invalid Input! A number between 1-10 must be provided. Try again...')
    #     search_books()

    # amount_of_books = input('\t-- How many copies do you want to add to the inventory?: ')

    # try:
    #     amount_of_books = int(amount_of_books)

    # except ValueError:
    #     print('\tInvalid Input! A number must be provided. Try again...')
    #     search_books()

    # to_add = input(f'\tConfirm adding {amount_of_books} copies of {book_obj.get_title()} to inventory (y/n): ') 
    # if to_add == 'y':
    #     inventory_json = db_functions.get_table_as_json_array(table_name = 'books') 
    #     inventory = library.Library.from_dict(inventory_json)
    #     inventory.add_book(book_obj,amount_of_books)
    #     print('\n\t\t Book was added successfully!\n')
    #     print(inventory)
    #     db_functions.add_book_to_books_table(book_json)