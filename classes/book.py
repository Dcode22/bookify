

class Book:
    def __init__(self, 
                 book_id : str, 
                 title : str, 
                 description : str, 
                 authors : str,
                 genre : str, 
                 published_date : str, 
                 language : str, 
                 page_count : int, 
                 cover_image_url : str, 
                 publisher : str, 
                 avg_rating : float,
                 maturity_rate : str,
                 buying_price : float,
                 selling_price : float,
                 amount_total : int = 1,
                 amount_available : int = 1) -> None:
        
        self.book_id = book_id
        self.title = title
        self.description = description
        self.authors = authors
        self.genre = genre
        self.published_date = published_date
        self.language = language
        self.page_count = page_count
        self.cover_image_url = cover_image_url
        self.publisher = publisher
        self.avg_rating = avg_rating
        self.maturity_rate = maturity_rate
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.amount_total = amount_total
        self.amount_available = amount_available


    def __str__(self) -> str:
        return f"{self.title} by {self.authors} ({self.published_date})"
    

    def is_in_stock(self) -> bool:
        return (self.amount_available > 0)
    

    def sell(self) -> bool:
        if (self.amount_available > 0):
            self.amount_available -= 1
            print("Product was sold successfully.")
            return True
        print("Failed! Not enough available stock.")
        return False
    

    def return_book(self):
        if (self.amount_available < self.amount_total):
            self.amount_available += 1
            print("Product was returned successfully.")
            return True
        print("Failed! Exceeding total amount in inventory. (Whether customer returned already or other reasons)")
        return False


    def update_book_amount(self, amount: int) -> None:
        self.amount_available += amount
        self.amount_total += amount


    def get_title(self):
        return self.title
    

    def to_dict (self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'description': self.description,
            'authors': self.authors,
            'genre': self.genre,
            'published_date': self.published_date,
            'language': self.language,
            'page_count': self.page_count,
            'cover_image_url': self.cover_image_url,
            'publisher': self.publisher,
            'avg_rating': self.avg_rating,
            'maturity_rate': self.maturity_rate,
            'buying_price' : self.buying_price,
            'selling_price' : self.selling_price,
            'amount_total': self.amount_total,
            'amount_available': self.amount_available
        }
    

    @classmethod
    def from_dict(cls, book_dict: dict) -> 'Book':
        return cls(
            book_dict['book_id'],
            book_dict['title'],
            book_dict['description'],
            book_dict['authors'],
            book_dict['genre'],
            book_dict['published_date'],
            book_dict['language'],
            book_dict['page_count'],
            book_dict['cover_image_url'],
            book_dict['publisher'],
            book_dict['avg_rating'],
            book_dict['maturity_rate'],
            book_dict.get('amount_total', 1),
            book_dict.get('amount_available', 1)
        )