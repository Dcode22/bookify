import api_functions
import db_functions
from classes.library import Library
from classes.book import Book

 


def search_books():  

    print(
        '''
+--------------+
| Search books |
+--------------+''')
    
    query = input("Search a book by title: ")
        
    search_results = api_functions.search_books(query, 10)

    if search_results:
        display_search_results(search_results)
        print("[b] to go back...\n")
        choice = input("To add a book to the inventory, enter the id (1-10), or type 'b' to go back: ")
        if choice == 'b':
            return

        try:
            id = int(choice)
            if id not in range(1,11):
                raise ValueError
        except ValueError:
            print("Invalid input. Must provide an integer between 1-10.")
            search_books()
        user_selected_book_json = search_results[id-1]

        try:
            amount = int(input("How many copies do you want to add to the inventory?: "))
        except ValueError:
            print("Invalid input. Must provide a whole number.")
            search_books()
        user_selected_book_json['amount_total'] = user_selected_book_json['amount_available'] = amount

        to_add = input(f"Confirm adding {amount} copies of {user_selected_book_json['title']} to inventory (y/n): ")
        if (to_add == 'y'):
            db_functions.add_book_to_books_table(user_selected_book_json)
            print("Book was added successfuly.")



def display_search_results(search_results :list[dict]) -> None:
    print(f"Top {len(search_results)} books matching your results: ")
    print("ID | TITLE")
    for id,result in enumerate(search_results):
        print(f"[{id+1}]| {result['title']}") #id starts with 0, so changed it to id+1