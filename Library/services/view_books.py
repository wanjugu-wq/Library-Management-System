from ..models.book import Book

def view_books():
    if len(Book.books) == 0:
        print("No books available!")

    for item in Book.books:
        print(f"\n Book: {item.title}\n Author: {item.author}\n Status: {item.status}\n Copies: {item.copies} ")