class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        # print(self._books)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True
                # print(f"{book.title} have been checked out.")
                return book

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                # print(f"{book.title} have been returned.")
                return book

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} is available.")
