from models.book import Book

def return_book():
   count = 0
   for item in Book.books:
      count = count + 1
      print(f"{count}. {item.title}")
   print("\nIf book is not in list, enter 0")

   choice = int(input("Enter the book you want to return: "))

   if choice == 0:
      book_returned = input("Enter name of the book: ")
      print(f"\n{book_returned} has been returned and staff have been informed. Thankyou!")
      return

   if choice < 0 or choice > len(Book.books):
      print("Invalid choice. Try again.")
      return
   else:
        book_choice = Book.books[choice -1]
        new_copies = book_choice.copies + 1
        book_choice.copies = new_copies
        print("\nBook returned successfully!")
    

   
