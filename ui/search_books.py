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

        try:
            id = int(input("\n\tTo add a book to the inventory, enter the id (1-10): "))
            if id not in range(1,11):
                raise ValueError
        except ValueError:
            print("Invalid input. Must provide an integer between 1-10.")
            search_books()
        user_selected_book_json = search_results[id-1]

        try:
            amount = int(input("\tHow many copies do you want to add to the inventory?: "))
        except ValueError:
            print("Invalid input. Must provide a whole number.")
            search_books()
        user_selected_book_json['amount_total'] = user_selected_book_json['amount_available'] = amount

        to_add = input(f"\tConfirm adding {amount} copies of {user_selected_book_json['title']} to inventory (y/n): ")
        if (to_add == 'y'):
            db_functions.add_book_to_books_table(user_selected_book_json)
            print("\tBook was added successfuly.")



def display_search_results(search_results :list[dict]) -> None:
    print(f"\tTop {len(search_results)} books matching your results: ")
    print("\tID | TITLE")
    for id,result in enumerate(search_results):
        print(f"\t[{id+1}]| {result['title']}") #id starts with 0, so changed it to id+1