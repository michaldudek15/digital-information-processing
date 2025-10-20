"""
Klasa Library ma listę obiektów Book. 
Metoda add_book() dodaje książkę.
Metoda show_books() wypisuje "Tytuł — Autor".
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(f"{book.title} — {book.author}")

library = Library()
library.add_book(Book("Folwark zwierzęcy", "George Orwell"))
library.add_book(Book("Normalni ludzie", "Sally Rooney"))
library.show_books()