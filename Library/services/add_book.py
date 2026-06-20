from models.book import Book

def add_book():
    book = input("\nEnter book title: ")
    author = input("Enter book author: ")
    copies = input("Enter number of available copies: ")

    Book(book,author,copies)

    print(f"\n{book} by {author} successfully added to library! Available copies: {copies}")