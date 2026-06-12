"""Problem 6: Library Book Availability System 
Problem Statement 
The number of available copies of books in a library is stored below. 
Sample Data 
books = { 
    "Python": 5, 
    "Java": 2, 
    "DBMS": 4, 
    "Networking": 1, 
    "OS": 3, 
    "AI": 6, 
    "ML": 2, 
    "Cloud": 5, 
    "Cyber Security": 1, 
    "Web Development": 4 
} 
Tasks 
1. Display books with fewer than 3 copies.  
2. Find the book with maximum copies.  
3. Find the book with minimum copies.  
4. Count total books available.  
5. Generate a restocking list.  
Sample Output 
Books Requiring Attention: 
Java 
Networking 
ML 
Cyber Security 
 
Book with Maximum Copies: 
AI (6 copies) 
 
Book with Minimum Copies: 
Networking (1 copy) 
 
Total Copies Available: 33 
 
Restocking List: 
['Java', 'Networking', 'ML', 'Cyber Security']"""

# Library Book Availability System

books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}
"""use for to keep key and value safe by . get"""

# 1. Display books with fewer than 3 copies
print("Books Requiring Attention:")
restocking_list = []

for book, copies in books.items():
    if copies < 3:
        print(book)
        restocking_list.append(book)

# 2. Find the book with maximum copies
max_book = max(books, key=books.get)

# 3. Find the book with minimum copies
min_book = min(books, key=books.get)

# 4. Count total books available
total_copies = sum(books.values())

# Display results
print("\nBook with Maximum Copies:")
print(max_book, "({books[max_book]} copies)")

print("\nBook with Minimum Copies:")
print(min_book, "({books[min_book]} copies)")

print("\nTotal Copies Available:")
print(total_copies)

# 5. Generate a restocking list
print("\nRestocking List:")
print(restocking_list)