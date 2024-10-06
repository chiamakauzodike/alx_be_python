#library_management.py

class Book:
    def __init__(self, title, author):
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
    def __init__(self):
        self._books = []
        
    def add_book(self, book):
        self._books.append(book)
        print(f"Book '{book.tile}' by (book.author} added to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Book '{title}' has been checked out.")
                    return
                else:
                    print(f"Book '{title}' is already checked out")
        print(f"Book '{title}' not in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_avaible():
                    book.return_book()
                    print(f"Book '{title}' returned.")
                    return
                else:
                    print(f"Book '{title}' was not checked out.")
                    return
         print(f"Book '{title}' was not found in the library.")
         
    def list_available_books(self):
         available_books = [book for book in self._books if book.is_available()]
         if available_books:
             print("Available books:")
             for book in available_books:
                 print(f"- {book.title} by {book.author}")
        else:
            print("No books available at the moment in the library.")

    
