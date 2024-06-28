from book import Book
from customer import Customer
import psycopg2
import db_functions


class Library:
    def __init__(self , budget: int, markup : float) -> None:
        self.inventory = []
        self.inventory_size = 0
        self.budget = budget
        self.markup = markup


    def fetch_books_from_database(self):
        self.inventory = db_functions.fetch_books_from_database()
        self.update_inventory_size()
    

    def __str__(self) -> str: 
        if not self.inventory:
            return "The library inventory is empty."
        inventory_summary = '\n'.join(book.__str__() for book in self.inventory)
        return f"Library Inventory: \n{inventory_summary}"
    
       
    def update_inventory_size(self) -> None:
        self.inventory_size = len(self.inventory)


    def get_inventory_size(self) -> int:
        return self.inventory_size


    def search_book(self, query: str) -> list:
        results = []
        query = query.lower()
        for book in self.inventory:
            if query in book.title.lower() or query in book.authors.lower():
                results.append(book)
        return results


    def check_availability(self, book_id : int) -> bool:
        book = self.search_book(book_id)
        if book and book.is_in_stock:
            return True
        return False
    

    def can_add_book(self, book : 'Book', amount : int):
        budget = self.budget
        total_buying_price = book.buying_price * amount
        return budget >= total_buying_price
    

    def add_book (self, book : 'Book', amount) -> None:
        book.selling_price = book.buying_price * self.markup
        book.update_book_amount(amount)
        self.inventory.append(book)
        self.update_inventory_size()


    def remove_book (self, book : 'Book') -> None:
        self.inventory.remove(book)
        self.update_inventory_size()

    
    def sell_to_customer(self, customer : 'Customer', book : 'Book', amount : int =1, ):
        price = book.selling_price
        self.budget += price
        customer.add_book(book)