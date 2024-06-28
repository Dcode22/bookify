import api_functions






def main():
    welcome_msg = '''
    ------------Welcome to Bookify!------------
    ---The World's #1 Book Management System---'''
    
    menu_msg = ''' 
        Menu :
        (1) Search books
        (2) Open inventory
        (3) Manage customers 
        (x) Exit
        Choose an option >> '''
    
    print(welcome_msg)
    while True:
        choice = input(menu_msg)

        if choice == 1:
            query = input("Enter a search query: ")
            list_of_books_results = api_functions.search_books(query) #search_books function is needed. return here a list of book objects. randomize a price for the book object
            for book in list_of_books_results:
                print(book) #Book.__str__() function is needed. return here each book with its details

            to_add_to_inventory = input("Would you like to add any of the books here to your inventory? 'y'/'n': ")
            if to_add_to_inventory == 'y':
                book_id = input("Please provide the desired book id: ")
                amount = int(input("Please provide an amount: "))

                #Check if book exists in search results
                is_book_id_exist = False
                for book in list_of_books_results:
                    if book.book_id == book_id:
                        is_book_id_exist = True

                    

                #Check if library budget can afford ordering the books
                can_library_afford = l

                #Add the books to the library. Check first if book exists. if so- change the book availability amount. if not- create a new book and append. Make sure to update the library budget
            






if __name__ == '__main__':
    main()