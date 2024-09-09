from abc import ABC, abstractmethod
from datetime import datetime

class StringValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, '')

    def __set__(self, instance, value):
        if instance is None:
            return self
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")
        instance.__dict__[self.name] = value

class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if instance is None:
            return self
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        instance.__dict__[self.name] = value

class Book(ABC):
    title = StringValue()
    author = StringValue()
    publication_date = StringValue()

    def __init__(self, title: str, author: str, publication_date: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.available: bool = True

    @abstractmethod
    def book_type(self) -> str:
        ...

class FictionBook(Book):
    def book_type(self) -> str:
        return "Fiction"

class NonFictionBook(Book):
    def book_type(self) -> str:
        return "Non-Fiction"

class Borrower:
    name = StringValue()
    contact_info = StringValue()

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.borrowing_history = []
        self.borrowed_books = []

    def search_book(self, library, title: str):
        return library.search_book(title)

    def borrow_book(self, library: 'Library', title: str) -> bool:
        book = library.borrow_book(self, title)
        if book:
            self.borrowed_books.append(book)
            self.borrowing_history.append((book.title, datetime.now()))
            return True
        return False

    def return_book(self, library, title: str) -> bool:
        for book in self.borrowed_books:
            if book.title == title:
                library.return_book(self, book)
                self.borrowed_books.remove(book)
                return True
        return False

    def view_borrowing_history(self):
        return self.borrowing_history

class Librarian:
    name = StringValue()
    contact_info = StringValue()

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def add_book(self, library, book: Book):
        library.add_book(book)

    def remove_book(self, library, title: str):
        library.remove_book(title)

class LibraryOperation(ABC):
    @abstractmethod
    def search_book(self, title: str):
        pass

    @abstractmethod
    def borrow_book(self, borrower: Borrower, title: str):
        pass

    @abstractmethod
    def return_book(self, borrower: Borrower, book: Book) :
        pass

    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

class Library(LibraryOperation):
    def __init__(self):
        self.books = []

    def search_book(self, title: str):
        for book in self.books:
            if book.title == title and book.available:
                return book
        return None

    def borrow_book(self, borrower: Borrower, title: str):
        book = self.search_book(title)
        if book:
            book.available = False
            return book
        return None

    def return_book(self, borrower: Borrower, book: Book):
        book.available = True

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

