# Library Management System

## About the Project

This project is a Python-based Library Management System designed to help libraries manage books and users easily. It allows adding, removing, searching, borrowing, and returning books, while keeping track of users and their borrowed books.

## Key Features

- Add new books and remove old ones from the library.
- Search for books by title or author.
- View all books or only those currently available.
- Register users and track the books they borrow.
- Borrow and return books with automatic availability checks.
- Display a user's borrowing history.
- Custom exceptions to handle common errors gracefully.

## Classes and What They Do

### Exceptions

- `BookNotFoundError`: Raised when a book cannot be found in the library.
- `BookNotAvailableError`: Raised when trying to borrow a book that is already borrowed.
- `UserNotFoundError`: Raised when a user cannot be found in the system.

### Book

Represents a single book in the library.

- `__init__(self, title, author, isbn, available=True)`: Create a new book.
- `display_info()`: Print the book's details.
- `borrow()`: Borrow the book if it’s available.
- `return_book()`: Return the book if it was borrowed.

### User

Represents a library user.

- `__init__(self, name, id)`: Create a new user.
- `borrow_book(book)`: Borrow a book.
- `return_book(book)`: Return a book.
- `display_borrowed()`: See all books currently borrowed by the user.

### Library

Represents the library itself.

- `__init__(self, name)`: Create a new library.
- `add_book(book)`: Add a book to the library.
- `remove_book(isbn)`: Remove a book by ISBN.
- `search_by_title(title)`: Search for books by title.
- `search_by_author(author)`: Search for books by author.
- `list_available()`: Show all available books.
- `list_all_books()`: Show all books in the library.
- `register_user(user)`: Add a new user to the system.
- `find_user(id)`: Find a user by their ID.

## Example Usage

```python
# Create some books
book1 = Book("harry potter", "j.k. rowling", "978-0-439-13959-8")
book2 = Book("the hobbit", "j.r.r. tolkien", "978-0-261-10221-7")
book3 = Book("clean code", "robert c. martin", "978-0-13-235088-4")

# Set up the library
lib = Library("Central")
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

# Register users
user1 = User("Wael", 101)
user2 = User("Ali", 102)
lib.register_user(user1)
lib.register_user(user2)

# Borrow and return books
user1.borrow_book(book1)  # Success
user2.borrow_book(book1)  # Fails, already borrowed
user1.return_book(book1)
user2.return_book(book1)  # Fails, didn't borrow

# See borrowed books
user1.display_borrowed()

# Search for books
for b in lib.search_by_title("clean"):
    b.display_info()

for b in lib.search_by_author("J.K. Rowling"):
    b.display_info()

# Remove a book
lib.remove_book("978-0-261-10221-7")

# List books
lib.list_all_books()
lib.list_available()
```

## Tech Stack

- Python 3.x

## Skills Gained

- Object-Oriented Programming (OOP) in Python
- Exception handling for robust code
- Working with lists and comprehensions
- Designing classes and methods effectively
- Building a simple, functional system from scratch

## Takeaways

This project helped me understand how to structure an object-oriented program, handle errors properly, and create a small but functional library management system. It’s a great example of applying Python skills to a real-world scenario.
