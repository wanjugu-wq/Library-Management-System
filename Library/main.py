from utils.storage import save_books, load_books
from Library.helpers.menu import system
from Library.services.add_book import add_book
from Library.services.view_books import view_books
from Library.services.borrow_book import borrow_book
from Library.services.remove_book import remove_book
from Library.services.return_book import return_book


def program():
    load_books()
    run = True

    while run:
        system()
        selected = input("\nEnter your selected function: ")
        
        if selected == "1":
            add_book()
        elif selected == "2":
            view_books()
        elif selected == "3":
            borrow_book()
        elif selected == "4":
            remove_book()
        elif selected == "5":
            return_book()
        elif selected == "6":
            save_books()
            print("\nExiting the system...")
            run = False
            return
        else:
            print("Invalid choice. Try again!")

program()