"""2. Library Book Issue System 
Problem Statement 
A library stores book information in books.txt. 
File Format 
B101,Python Basics,5 
B102,Java Programming,2 
B103,Data Science,0 
B104,DBMS,3 
B105,Machine Learning,1 
B106,Operating Systems,4 
B107,Networking,2 
B108,Cyber Security,6 
B109,Cloud Computing,0 
B110,Web Development,3 
Requirements 
Develop a program to: 
1. Display all books.  
2. Search a book using Book ID.  
3. Issue a book (decrease quantity by 1).  
4. Return a book (increase quantity by 1).  
5. Display unavailable books.  
6. Display books requiring restocking (copies < 2).  
7. Update the file after every issue/return operation. 
"""
# Library Book Issue System

while True:

    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book by ID")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # ===================================
    # Display All Books
    # ===================================
    if choice == 1:

        file = open('books.txt', 'r')

        print("\nBook Records:")

        for line in file:
            print(line.strip())

        file.close()

    # ===================================
    # Search Book by ID
    # ===================================
    elif choice == 2:

        book_id = input("Enter Book ID: ")

        file = open('books.txt', 'r')

        found = False

        for line in file:

            data = line.strip().split(",")

            if data[0] == book_id:

                print("\nBook Found")
                print("Book ID :", data[0])
                print("Book Name :", data[1])
                print("Quantity :", data[2])

                found = True

        if found == False:
            print("Book Not Found")

        file.close()

    # ===================================
    # Issue Book
    # ===================================
    elif choice == 3:

        book_id = input("Enter Book ID: ")

        file = open('books.txt', 'r')

        books = []

        for line in file:

            data = line.strip().split(",")

            if data[0] == book_id:

                quantity = int(data[2])

                if quantity > 0:
                    quantity = quantity - 1
                    print("Book Issued Successfully")
                else:
                    print("Book Not Available")

                data[2] = str(quantity)

            books.append(",".join(data))

        file.close()

        file = open("books.txt", "w")

        for record in books:
            file.write(record + "\n")

        file.close()

    # ===================================
    # Return Book
    # ===================================
    elif choice == 4:

        book_id = input("Enter Book ID: ")

        file = open('books.txt', 'r')

        books = []

        for line in file:

            data = line.strip().split(",")

            if data[0] == book_id:

                quantity = int(data[2])

                quantity = quantity + 1

                data[2] = str(quantity)

                print("Book Returned Successfully")

            books.append(",".join(data))

        file.close()

        file = open('books.txt', 'w')

        for record in books:
            file.write(record + "\n")

        file.close()

    # ===================================
    # Unavailable Books
    # ===================================
    elif choice == 5:

        file = open('books.txt', 'r')

        print("\nUnavailable Books:")

        for line in file:

            data = line.strip().split(",")

            if int(data[2]) == 0:
                print(data[0], data[1])

        file.close()

    # ===================================
    # Restocking Required
    # ===================================
    elif choice == 6:

        file = open('books.txt', 'r')

        print("\nBooks Requiring Restocking:")

        for line in file:

            data = line.strip().split(",")

            if int(data[2]) < 2:
                print(data[0], data[1], data[2])

        file.close()

    # ===================================
    # Exit
    # ===================================
    elif choice == 7:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")
