import uuid

class Book:
    number_of_books = 0
    books = []

    def __init__(self,title,author,copies,status = "Available"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.status = status
        self.copies = copies
        Book.number_of_books += 1
        Book.books.append(self)
    
    @property
    def copies(self):
        return self._copies
    
    @copies.setter
    def copies(self,value):
        value = int(value)
        if not isinstance(value,int):
            raise ValueError("Copies needs to be a number type")
        
        if value < 0:
            raise ValueError("Copies cannot be a negative value")
        
        self._copies = value
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        value = value.strip()

        if value == "":
            raise ValueError("Title cannot be empty.")
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        value = value.strip()
        if not isinstance(value, str):
            raise ValueError("Author must be a string.")
        if value == "":
            raise ValueError("Author cannot be empty.")
        
        self._author = value

    def __repr__(self):
        return f" Book: {self.title}\n Author: {self.author}\n Status: {self.status}\n Copies: {self.copies}"