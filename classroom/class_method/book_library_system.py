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

    def _init_(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print(f"\n'{self.title}' has been issued successfully.")
        else:
            print(f"\nSorry! '{self.title}' is already issued.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"\n'{self.title}' has been returned successfully.")
        else:
            print(f"\n'{self.title}' is already available in the library.")

    def display_details(self):
        status = "Available" if self.available else "Issued"

        print("\n========== BOOK DETAILS ==========")
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Status  :", status)
        print("==================================")


# ---------------- MAIN PROGRAM ----------------

try:
    book_id = int(input("Enter Book ID: "))

    title = input("Enter Book Title: ").strip()
    if not title:
        raise ValueError("Title cannot be empty.")

    author = input("Enter Author Name: ").strip()
    if not author:
        raise ValueError("Author name cannot be empty.")

    book = Book(book_id, title, author)

    while True:

        print("\n===== LIBRARY MENU =====")
        print("1. Display Book Details")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book.display_details()

        elif choice == "2":
            book.issue_book()

        elif choice == "3":
            book.return_book()

        elif choice == "4":
            print("\nThank you for using the Library System.")
            break

        else:
            print("\nInvalid choice. Please try again.")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
    