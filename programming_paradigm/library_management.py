class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def _init_(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out: {title}")
                    return True
        print(f"Book not available: {title}")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Returned: {title}")
                    return True
        print(f"Book not found or not checked out: {title}")
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
