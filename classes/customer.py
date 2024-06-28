from book import Book

class Customer:
    def __init__(self, customer_id : int, first_name : str, last_name : str, email : str, phone : str, books_list : list['Book']):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.books_list = books_list

    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} (ID: {self.customer_id})"


    def update_email(self, new_email: str) -> None:
        self.email = new_email

    def update_phone(self, new_phone: str) -> None:
        self.phone = new_phone

    
    def to_dict(self) -> dict:
        return {
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'books_list' : self.books_list
        }
    

    @classmethod
    def from_dict(cls, customer_dict : dict) -> 'Customer':
        return cls(
            customer_dict['customer_id'],
            customer_dict['first_name'],
            customer_dict['last_name'],
            customer_dict['email'],
            customer_dict['phone'],
            customer_dict['books_list']
        )