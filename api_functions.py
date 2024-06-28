import requests

API_KEY = 'AIzaSyCXTZkmqAbEoXaEPX-etOG-BSFVZuwN_K4'

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

            list_of_filtered_books.append({
                'id': book.get('id'),
                'title': volume_info.get('title'),
                'authors': volume_info.get('authors'),
                'publisher': volume_info.get('publisher'),
                'publishedDate': volume_info.get('publishedDate'),
                'description': volume_info.get('description'),
                'pageCount': volume_info.get('pageCount'),
                'genre': volume_info.get('categories'),
                'averageRating': volume_info.get('averageRating'),
                'maturityRating': volume_info.get('maturityRating'),
                'smallThumbnail': image_links.get('smallThumbnail'),
                'language': volume_info.get('language')
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

books_list = search_books("Harry Potter", 5)

def select_a_single_book(book_id: str) -> dict:
    for book in books_list:
        if book['id'] == book_id:
            return book
    return None 

# print(f"==>> books_list: {books_list}")
# selected_book = select_a_single_book('JGQBcu5O_ZcC')     
# print(f"==>> selected_book: {selected_book}")

