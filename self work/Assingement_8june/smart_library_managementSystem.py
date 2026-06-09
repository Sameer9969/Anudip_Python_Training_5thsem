"""3. Smart Library Management System 
Problem Statement 
Create a digital library management system. 
Example Structure 
library = { 
    "B101": { 
        "title": "Python Basics", 
        "author": "ABC", 
        "copies": 5 
    } 
} 
Maintain records of at least 30 books. 
Requirements 
1. Add a book.  
2. Remove a book.  
3. Search a book by ID.  
4. Search by title.  
5. Update available copies.  
6. Issue a book.  
7. Return a book.  
8. Display books with fewer than 3 copies.  
9. Display books that are unavailable.  
10. Find the most available book.  
11. Generate a restocking report.  
12. Create a separate dictionary of books requiring immediate purchase. """


# ==========================================
# SMART LIBRARY MANAGEMENT SYSTEM
# ==========================================

# Nested Dictionary bana rahe hain
# Har Book ID ke andar title, author aur copies store hain
library = {
    "B101": {"title": "Python Basics", "author": "John Doe", "copies": 5},
    "B102": {"title": "Data Structures", "author": "Ellis Horowitz", "copies": 2},
    "B103": {"title": "Web Development", "author": "Angela Yu", "copies": 8},
    "B104": {"title": "Machine Learning", "author": "Andrew Ng", "copies": 0},
    "B105": {"title": "Let Us C", "author": "Yashavant Kanetkar", "copies": 12}
}

# Infinite loop start
while True:

    # Menu display
    print("\n==============================")
    print("SMART LIBRARY MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book By ID")
    print("4. Search Book By Title")
    print("5. Update Copies")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Low Copies Books")
    print("9. Unavailable Books")
    print("10. Most Available Book")
    print("11. Restocking Report")
    print("12. Immediate Purchase Dictionary")
    print("13. Exit")

    # User se choice lena
    choice = input("Enter Choice : ")

    # =====================================
    # OPTION 1 : ADD BOOK
    # =====================================
    if choice == "1":

        # New Book ID lena
        bid = input("Enter Book ID : ").upper()

        # Check karna ki ID pehle se hai ya nahi
        if bid in library:

            # Agar hai to error
            print("Book ID Already Exists")

        else:

            # Title input lena
            title = input("Enter Title : ")

            # Author input lena
            author = input("Enter Author : ")

            # Copies input lena
            copies = int(input("Enter Copies : "))

            # Copies valid honi chahiye
            if copies >= 0:

                # New book dictionary me add karna
                library[bid] = {
                    "title": title,
                    "author": author,
                    "copies": copies
                }

                # Success message
                print("Book Added Successfully")

            else:

                # Invalid copies
                print("Copies Cannot Be Negative")

    # =====================================
    # OPTION 2 : REMOVE BOOK
    # =====================================
    elif choice == "2":

        # Book ID lena
        bid = input("Enter Book ID : ").upper()

        # Check karna ki book exist karti hai ya nahi
        if bid in library:

            # Book delete karna
            del library[bid]

            # Success message
            print("Book Removed Successfully")

        else:

            # Book nahi mili
            print("Book Not Found")

    # =====================================
    # OPTION 3 : SEARCH BOOK BY ID
    # =====================================
    elif choice == "3":

        # Book ID lena
        bid = input("Enter Book ID : ").upper()

        # Book search karna
        if bid in library:

            # Book details print karna
            print("Title :", library[bid]["title"])
            print("Author :", library[bid]["author"])
            print("Copies :", library[bid]["copies"])

        else:

            # Book nahi mili
            print("Book Not Found")

    # =====================================
    # OPTION 4 : SEARCH BOOK BY TITLE
    # =====================================
    elif choice == "4":

        # Search title lena
        search_title = input("Enter Title : ").lower()

        # Book found flag
        found = False

        # Dictionary traverse karna
        for bid in library:

            # Title match karna
            if search_title in library[bid]["title"].lower():

                # Book details print karna
                print(
                    bid,
                    library[bid]["title"],
                    library[bid]["author"],
                    library[bid]["copies"]
                )

                # Found flag true karna
                found = True

        # Agar book na mile
        if found == False:

            print("Book Not Found")

    # =====================================
    # OPTION 5 : UPDATE COPIES
    # =====================================
    elif choice == "5":

        # Book ID lena
        bid = input("Enter Book ID : ").upper()

        # Check karna book hai ya nahi
        if bid in library:

            # New copies lena
            new_copies = int(input("Enter New Copies : "))

            # Copies update karna
            library[bid]["copies"] = new_copies

            # Success message
            print("Copies Updated Successfully")

        else:

            # Book nahi mili
            print("Book Not Found")

    # =====================================
    # OPTION 6 : ISSUE BOOK
    # =====================================
    elif choice == "6":

        # Book ID lena
        bid = input("Enter Book ID : ").upper()

        # Check karna book hai ya nahi
        if bid in library:

            # Copies available hain ya nahi
            if library[bid]["copies"] > 0:

                # 1 copy kam karna
                library[bid]["copies"] -= 1

                # Success message
                print("Book Issued Successfully")

            else:

                # Copies available nahi
                print("Book Out Of Stock")

        else:

            # Book nahi mili
            print("Book Not Found")

    # =====================================
    # OPTION 7 : RETURN BOOK
    # =====================================
    elif choice == "7":

        # Book ID lena
        bid = input("Enter Book ID : ").upper()

        # Book exist karti hai ya nahi
        if bid in library:

            # 1 copy increase karna
            library[bid]["copies"] += 1

            # Success message
            print("Book Returned Successfully")

        else:

            # Book nahi mili
            print("Book Not Found")

    # =====================================
    # OPTION 8 : LOW COPIES BOOKS
    # =====================================
    elif choice == "8":

        # Heading print karna
        print("\nBooks With Less Than 3 Copies")

        # Dictionary traverse karna
        for bid in library:

            # Copies check karna
            if library[bid]["copies"] < 3:

                # Book print karna
                print(
                    bid,
                    library[bid]["title"],
                    library[bid]["copies"]
                )

    # =====================================
    # OPTION 9 : UNAVAILABLE BOOKS
    # =====================================
    elif choice == "9":

        # Heading print karna
        print("\nUnavailable Books")

        # Dictionary traverse karna
        for bid in library:

            # Copies zero hain ya nahi
            if library[bid]["copies"] == 0:

                # Book print karna
                print(
                    bid,
                    library[bid]["title"]
                )

    # =====================================
    # OPTION 10 : MOST AVAILABLE BOOK
    # =====================================
    elif choice == "10":

        # First book ko max maan lena
        max_bid = list(library.keys())[0]

        # Dictionary traverse karna
        for bid in library:

            # Compare copies
            if library[bid]["copies"] > library[max_bid]["copies"]:

                # New maximum book
                max_bid = bid

        # Result print karna
        print(
            "Most Available Book :",
            library[max_bid]["title"]
        )

        print(
            "Copies :",
            library[max_bid]["copies"]
        )

    # =====================================
    # OPTION 11 : RESTOCKING REPORT
    # =====================================
    elif choice == "11":

        # Heading print karna
        print("\nRestocking Report")

        # Dictionary traverse karna
        for bid in library:

            # Low stock check karna
            if library[bid]["copies"] < 3:

                # Report print karna
                print(
                    bid,
                    library[bid]["title"],
                    library[bid]["copies"]
                )

    # =====================================
    # OPTION 12 : IMMEDIATE PURCHASE
    # =====================================
    elif choice == "12":

        # Empty dictionary banana
        immediate_purchase = {}

        # Dictionary traverse karna
        for bid in library:

            # Copies less than 2
            if library[bid]["copies"] < 2:

                # New dictionary me add karna
                immediate_purchase[bid] = library[bid]

        # Dictionary print karna
        print(immediate_purchase)

    # =====================================
    # OPTION 13 : EXIT
    # =====================================
    elif choice == "13":

        # Exit message
        print("Thank You")

        # Loop stop karna
        break

    # =====================================
    # INVALID CHOICE
    # =====================================
    else:

        # Error message
        print("Invalid Choice")