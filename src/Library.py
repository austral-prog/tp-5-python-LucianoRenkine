from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []

    # Getters
    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def get_checked_out_books(self):
        return self.__checked_out_books

    def get_checked_in_books(self):
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn, title, author):
        new_book = Book(isbn, title, author)
        self.__books.append(new_book)

    # 1.2 List All Books
    def list_all_books(self):
        for book in self.__books:
            print(f"ISBN: {book.get_isbn()}, Title: {book.get_title()}, Author: {book.get_author()}")

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date):
        for book in self.__books:
            if book.get_isbn() == isbn and book.is_available():
                for user in self.__users:
                    if user.get_dni() == dni:
                        book.set_available(False)
                        self.__checked_out_books.append((book, user, due_date))
                        return f"User {dni} checked out book {isbn}"
        return f"Book {isbn} is not available"

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date):
        for checked_out in self.__checked_out_books:
            book, user, due_date = checked_out
            if book.get_isbn() == isbn and user.get_dni() == dni:
                book.set_available(True)
                self.__checked_out_books.remove(checked_out)
                self.__checked_in_books.append((book, user, returned_date))
                return f"Book {isbn} checked in by user {dni}"
        return f"Book {isbn} not checked out by user {dni}"

    # Utils
    def add_user(self, dni, name):
        new_user = User(dni, name)
        self.__users.append(new_user)
