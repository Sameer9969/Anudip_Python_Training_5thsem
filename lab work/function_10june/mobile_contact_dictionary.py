"""4. Mobile Contact Directory System 
Problem Statement 
Contacts are stored in contacts.txt. 
File Format 
Anuj,9876543210 
Rahul,9876543211 
Priya,9876543212 
Neha,9876543213 
Amit,9876543214 
Sneha,9876543215 
Karan,9876543216 
Pooja,9876543217 
Rohit,9876543218 
Anjali,9876543219 
Requirements 
Create a menu-driven application to: 
1. Display all contacts.  
2. Search a contact by name.  
3. Add a new contact.  
4. Update an existing contact number.  
5. Delete a contact.  
6. Display contacts whose names start with a vowel.  
7. Save all modifications back to the file.  """


# Mobile Contact Directory System

# Contacts store karne ke liye empty list
contacts = []

# contacts.txt file ko read mode me open kar rahe hain
file = open("contacts.txt", "r")

# File ki har line ko read karenge
for line in file:

    # Extra newline remove kar rahe hain
    line = line.strip()

    # Name aur number ko comma se alag kar rahe hain
    data = line.split(",")

    # Name store kar rahe hain
    name = data[0]

    # Mobile number store kar rahe hain
    number = data[1]

    # List me contact add kar rahe hain
    contacts.append([name, number])

# File close kar rahe hain
file.close()

# Menu ko repeat karne ke liye infinite loop
while True:

    print("\n===== CONTACT DIRECTORY =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Save and Exit")

    # User se choice le rahe hain
    choice = int(input("Enter your choice: "))

    # -----------------------------------
    # 1. Display All Contacts
    # -----------------------------------
    if choice == 1:

        print("\nALL CONTACTS")

        # Sabhi contacts print karenge
        for contact in contacts:
            print(contact[0], "-", contact[1])

    # -----------------------------------
    # 2. Search Contact
    # -----------------------------------
    elif choice == 2:

        # Search karne ke liye name input
        search_name = input("Enter Name: ")

        found = False

        # Contact list me search karenge
        for contact in contacts:

            if contact[0].lower() == search_name.lower():

                print("Name :", contact[0])
                print("Number :", contact[1])

                found = True
                break

        # Agar contact na mile
        if found == False:
            print("Contact Not Found")

    # -----------------------------------
    # 3. Add New Contact
    # -----------------------------------
    elif choice == 3:

        # Naya name input
        name = input("Enter Name: ")

        # Naya mobile number input
        number = input("Enter Number: ")

        # Contact list me add kar rahe hain
        contacts.append([name, number])

        print("Contact Added Successfully")

    # -----------------------------------
    # 4. Update Contact Number
    # -----------------------------------
    elif choice == 4:

        # Jiska number update karna hai
        update_name = input("Enter Name: ")

        found = False

        for contact in contacts:

            if contact[0].lower() == update_name.lower():

                # Naya number input
                new_number = input("Enter New Number: ")

                # Number update kar rahe hain
                contact[1] = new_number

                print("Contact Updated Successfully")

                found = True
                break

        if found == False:
            print("Contact Not Found")

    # -----------------------------------
    # 5. Delete Contact
    # -----------------------------------
    elif choice == 5:

        # Delete karne ke liye name input
        delete_name = input("Enter Name: ")

        found = False

        for contact in contacts:

            if contact[0].lower() == delete_name.lower():

                # Contact remove kar rahe hain
                contacts.remove(contact)

                print("Contact Deleted Successfully")

                found = True
                break

        if found == False:
            print("Contact Not Found")

    # -----------------------------------
    # 6. Contacts Starting With Vowel
    # -----------------------------------
    elif choice == 6:

        print("\nCONTACTS STARTING WITH VOWEL")

        for contact in contacts:

            # Name ka first letter check kar rahe hain
            first_letter = contact[0][0].lower()

            # Agar vowel hai to print karo
            if first_letter in ['a', 'e', 'i', 'o', 'u']:

                print(contact[0], "-", contact[1])

    # -----------------------------------
    # 7. Save and Exit
    # -----------------------------------
    elif choice == 7:

        # contacts.txt ko write mode me open kar rahe hain
        file = open("contacts.txt", "w")

        # Updated contacts file me save karenge
        for contact in contacts:

            file.write(contact[0] + "," + contact[1] + "\n")

        # File close kar rahe hain
        file.close()

        print("All Changes Saved Successfully")
        print("Thank You")

        # Program band kar rahe hain
        break

    # -----------------------------------
    # Invalid Choice
    # -----------------------------------
    else:

        print("Invalid Choice")

        # cd "lab work/function_10june"