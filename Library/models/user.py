import re

class User:
    def __init__(self,id,name,borrowed_books):
        self.id = id
        self.name = name
        self.books = borrowed_books
    
    @property
    def id(self):
           return self._id
    
    @id.setter
    def id(self,value):
        string = str(value)

        if len(string) != 8:
            raise ValueError("Id number should be 8 characters long")
        
        if not re.match(r"^\d+$",string):
               raise ValueError("Id must only contain numbers")
        
        self._id = string
                

    def __repr__(self):
                return f" Name: {self.name}\n Borrowed books: {self.books}\n "
    
user1 = User("22141844","Michelle Wanjugu","Book Theif")
print(user1)
print(user1.id)
