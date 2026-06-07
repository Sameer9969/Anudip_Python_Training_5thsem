"""Sample Data 
books = { 
    "Python Basics": 5, 
    "Data Structures": 0, 
    "Machine Learning": 3, 
    "Java Programming": 2, 
    "DBMS": 0, 
    "Operating Systems": 6, 
    "Networking": 4, 
    "Cloud Computing": 1, 
    "Cyber Security": 0, 
    "Web Development": 7 
} 
Tasks 
• Display books that are currently unavailable.  
• Count the number of available books.  
• Find the book with the maximum copies.  
• Create a list of books having less than 3 copies.  
• Calculate the total number of books available. """

# Library books dictionary
# Key = Book Name
# Value = Number of Copies Available

books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# ==================================================
# 1. Display books that are currently unavailable
# ==================================================

print("Books currently unavailable:")

# Loop through each book and its copies
for book, copies in books.items():

    # Check if copies are 0
    if copies == 0:

        # Print book name
        print(book)

# ==================================================
# 2. Count the number of available books
# ==================================================

# Variable to store count of available books
available_count = 0

# Loop through all copy values
for copies in books.values():

    # Check if at least 1 copy is available
    if copies > 0:

        # Increase count by 1
        available_count += 1

# Display total available books
print("Number of available books:", available_count)

# ==================================================
# 3. Find the book with the maximum copies
# ==================================================

# Variable to store book name
max_book = ""

# Variable to store maximum copies
max_copies = 0

# Loop through each book and copies
for book, copies in books.items():

    # Check if current copies are greater than max copies
    if copies > max_copies:

        # Update maximum copies
        max_copies = copies

        # Store book name
        max_book = book

# Display book with maximum copies
print("Book with maximum copies:", max_book)

# Display number of copies
print("Copies:", max_copies)

# ==================================================
# 4. Create a list of books having less than 3 copies
# ==================================================

# Empty list to store book names
less_than_3 = []

# Loop through each book and copies
for book, copies in books.items():

    # Check if copies are less than 3
    if copies < 3:

        # Add book name to list
        less_than_3.append(book)

# Display list
print("Books having less than 3 copies:", less_than_3)

# ==================================================
# 5. Calculate the total number of books available
# ==================================================

# Variable to store total copies
total_books = 0

# Loop through all copy values
for copies in books.values():

    # Add current copies to total
    total_books += copies

# Display total number of copies available
print("Total number of books available:", total_books)