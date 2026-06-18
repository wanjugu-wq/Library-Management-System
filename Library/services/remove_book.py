from ..models.book import Book

def remove_book():
   count = 0
   for item in Book.books:
      count = count + 1
      print(f"{count}. {item.title}")
   
   choice = int(input("\nEnter the book you want to remove: "))

   if choice < 1 or choice > len(Book.books):
      print("Invalid choice. Try again.")
      return
   
   Book.books.pop(choice - 1)

   print("Book removed successfully!")
