import requests
import random
from datetime import datetime

API_KEY = 'AIzaSyCXTZkmqAbEoXaEPX-etOG-BSFVZuwN_K4'

def parse_date(date_str):
    try:
        #try to parse YYYY-MM-DD
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None #otherwise, return None since that's the only format the postgres date column can accept



def search_books(book_name: str, amount_of_books: int) -> list:
    url = f'https://www.googleapis.com/books/v1/volumes?q={book_name}&key={API_KEY}'
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()

        list_of_books = data['items'][:amount_of_books]
        list_of_filtered_books = []

        for book in list_of_books:
            volume_info = book.get('volumeInfo', {})
            image_links = volume_info.get('imageLinks', {})

            buying_price = random.randint(20,30)
            selling_price = random.randint(60,129)

            published_date_str = volume_info.get('publishedDate', None)
            published_date = parse_date(published_date_str) if published_date_str else None

            list_of_filtered_books.append({
                'book_id': book.get('id'),
                'title': volume_info.get('title'),
                'description': volume_info.get('description',None),
                'authors': volume_info.get('authors',[None])[0],
                'genre': volume_info.get('categories',[None])[0],
                'published_date': published_date,
                'language': volume_info.get('language', None),
                'page_count': volume_info.get('pageCount', None),
                'cover_image_url': image_links.get('smallThumbnail', None),
                'publisher': volume_info.get('publisher', None),
                'avg_rating': volume_info.get('averageRating', None),
                'maturity_rate': volume_info.get('maturityRating', None),
                'buying_price' : buying_price,
                'selling_price' : selling_price,
                'amount_total' : None,
                'amount_available' : None
            })

        return list_of_filtered_books

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except KeyError:
        print("\tNo results for this search term. Try a different title...")

books_list = search_books("Harry Potter", 5)

def select_a_single_book(book_id: str) -> dict:
    for book in books_list:
        if book['id'] == book_id:
            return book
    return None 

# print(f"==>> books_list: {books_list}")
# selected_book = select_a_single_book('JGQBcu5O_ZcC')     
# print(f"==>> selected_book: {selected_book}")

