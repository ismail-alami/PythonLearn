class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', checked_out={self._is_checked_out})"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                print(f"Book '{title}' checked out successfully.")
                return
        print(f"Book '{title}' is either not available or already checked out.")


    def return_book(title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                 print(f"Book '{title}' is returned successfully.")
                return
        print(f"Book '{title}' is'nt available.")

    def list_available_books(self):
       book for book in self._books:
           if not book._is_checked_out:
                print(f"- {book.title} by {book.author}")
            print("No books available.")
    
