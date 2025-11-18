class BookNotFoundError(Exception):
    """ Raised when a book cannot be found in the library """
    pass

class BookNotAvailableError(Exception):
    """Raised when trying to borrow an unavailable book"""
    pass

class UserNotFoundError(Exception):
    """Raised when a user cannot be found in the system"""
    pass


class Book:
    """Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book.
        available (bool): Whether the book is available for borrowing.
    """
    def __init__(self,title,author,isbn,available=True):
        self.title = title.title()
        self.author = author.title()
        self.isbn = isbn
        self.available = available

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nStatus: {status}")
        print("----------------------------")

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed")
            return True
        else:
            print(f"Sorry, {self.title} is already borrowed")
            return False

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} returned Successfully")
            return True
        else:
            print(f"{self.title} Wasn't Borrowed")
            return False

class Library:
    """Represents a library with books and registered users.

    Attributes:
        name (str): Name of the library.
        books (list): List of Book objects in the library.
        users (list): List of User objects registered in the library.
    """
    def __init__(self,name):
        self.name = name.title()
        self.books = []
        self.users = []
        print(f"{self.name} Library Created Successfully")

    def add_book(self,book):
        self.books.append(book)
        print(f"{book.title} added to the {self.name} Library")

    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"{book.title} is Removed Successfully")
                return
        print(f"Book with ISBN {isbn} not found")

    def search_by_title(self,title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self,author):
        return [book for book in self.books if author.lower() == book.author.lower()]

    def list_available(self):
        """Prints all available books in the library."""
        available_books = [f"Title: {book.title} | Author: {book.author} | ISBN: {book.isbn}" for book in self.books if book.available]
        if available_books:
            print("Available Books:")
            for i in range(len(available_books)):
                 print(f"{i+1}. {available_books[i]}")
        else:
            print("No Books Available")

    def list_all_books(self):
        """Prints all books in the library with their availability status."""
        if not self.books:
            print("No Books Available")
            return
        else:
            print(f"All Books in {self.name} Library:")
            for book in self.books:
                status = "Available" if book.available else "Borrowed"
                print(f"Title: {book.title} | Author: {book.author} | ISBN: {book.isbn} | Status: {status}")
                print("-------------------------")
            print(f"{self.name} Library has {len(self.books)} Books")

    def register_user(self,user):
        """Registers a new user in the library."""
        self.users.append(user)
        print(f"User '{user.name}' registered to {self.name} Library")

    def find_user(self,id):
        if not self.users:  # True when No Users
            print(f"{self.name} Library has zero user.")
            return None
        else:
            for user in self.users:
                if user.user_id==id:
                    return user  # user found return user object
            print(f"User not found")
            return None

class User:
    """Represents a library user.

    Attributes:
        name (str): Name of the user.
        user_id (int): Unique ID of the user.
        borrowed_books (list): List of ISBNs of borrowed books.
    """
    def __init__(self,name,id):
        self.name = name.title()
        self.user_id = id
        self.borrowed_books = []

    def borrow_book(self,book):
            if book.borrow():
                print(f"Borrowed by {self.name}")
                self.borrowed_books.append(book.isbn)
                return True
            else:
                return False

    def return_book(self,book):
        if book.isbn in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.isbn)
            print(f"{self.name} return {book.title}")
            return True
        else:
            print(f"{self.name} didn't borrow {book.title}")
            return False

    def display_borrowed(self):
        """Displays all books currently borrowed by the user."""
        if self.borrowed_books:
            print(f"Books borrowed by {self.name}")
            for book in self.borrowed_books:
                print(f"ISBN: {book}")
            print(f"Total: {len(self.borrowed_books)} books")
        else:
            print(f"{self.name} has no borrowed books")
