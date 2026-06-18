import json
from models.book import Book


FILE_NAME = "data/books.json"


def save_books():
    data = []

    for book in Book.books:
        data.append({
            "title": book.title,
            "author": book.author,
            "copies": book.copies,
            "status": book.status
        })

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        for item in data:
            Book(
                title=item["title"],
                author=item["author"],
                copies=item["copies"],
                status=item["status"]
            )

    except FileNotFoundError:
        with open(FILE_NAME, "w") as file:
            json.dump([], file)

    except json.JSONDecodeError:
        print("books.json is corrupted.")