from ..models.book import Book

def borrow_book():
   count = 0
   for item in Book.books:
      count = count + 1
      print(f"{count}. {item.title}")
   
   choice = int(input("Enter the book you want to borrow: "))
   
   if choice < 1 or choice > len(Book.books):
      print("Invalid choice. Try again.")
      return
   
   book_choice = Book.books[choice -1]

   if book_choice.copies == 0:
      print("\nNo more copies available for you at this time. Sorry for the inconvinience! ")
      return
   else:
      new_copies = book_choice.copies - 1
      book_choice.copies = new_copies
      print("\nBook borrowed successfully!")

   if book_choice.copies == 0:
      book_choice.status = "Out of Stock"
