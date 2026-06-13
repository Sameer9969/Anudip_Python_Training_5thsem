"""5. Book Library System (Intermediate) 
Problem Statement: 
Create a Book class with attributes: 
• Book ID  
• Title  
• Author  
• Availability Status  
Implement methods to: 
• Issue a book.  
• Return a book.  
• Display book details.  
Prevent issuing a book that is already issued. 
Sample Output: 
Book Issued Successfully. 
Availability Status: Not Available"""


class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print("Book Issued")
        else:
            print("Book Already Issued")

    def return_book(self):
        self.available = True
        print("Book Returned")

    def display_details(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)


book = Book(101, "Python Basics", "John")

book.display_details()
book.issue_book()
book.issue_book()
book.return_book()
book.display_details()
book.return_book()
book.display_details()