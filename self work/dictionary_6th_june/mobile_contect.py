"""contacts = { 
    "Amit": "9876543210", 
    "Priya": "9876543211", 
    "Rohan": "9876543212", 
    "Neha": "9876543213", 
    "Anjali": "9876543214", 
    "Karan": "9876543215", 
    "Pooja": "9876543216", 
    "Arjun": "9876543217", 
    "Sneha": "9876543218", 
    "Rahul": "9876543219" 
} 
Tasks 
• Display all contact names in alphabetical order.  
• Count the total number of contacts.  
• Search for a given contact name.  
• Create a list of contacts whose names start with a vowel.  
• Stop the search using break once the required contact is found.  """


# Contact dictionary
# Key = Contact Name
# Value = Phone Number

contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# ==================================================
# 1. Display all contact names in alphabetical order
# ==================================================

print("Contacts in Alphabetical Order:")

# sorted() function names ko alphabetical order me arrange karti hai
for name in sorted(contacts.keys()):

    # Print contact name
    print(name)

# ==================================================
# 2. Count the total number of contacts
# ==================================================

# len() dictionary me total entries count karta hai
total_contacts = len(contacts)

# Display total contacts
print("Total Contacts:", total_contacts)

# ==================================================
# 3. Search for a given contact name
# ==================================================

# User se name input lo
search_name = input("Enter contact name to search: ")

# Check karo name dictionary me hai ya nahi
if search_name in contacts:

    # Contact mil gaya to number print karo
    print("Contact Found")
    print("Phone Number:", contacts[search_name])

else:

    # Contact nahi mila
    print("Contact Not Found")

# ==================================================
# 4. Create a list of contacts whose names start
#    with a vowel
# ==================================================

# Empty list create karo
vowel_contacts = []

# Dictionary ke sabhi names par loop
for name in contacts.keys():

    # Check karo first letter vowel hai ya nahi
    if name[0] in "AEIOUaeiou":

        # Name ko list me add karo
        vowel_contacts.append(name)

# Display list
print("Names starting with vowels:")
print(vowel_contacts)

# ==================================================
# 5. Stop the search using break once contact is found
# ==================================================

# User se name input lo
required_contact = input("Enter contact to search: ")

# Loop through all contact names
for name in contacts.keys():

    # Check karo current name required name ke equal hai ya nahi
    if name == required_contact:

        # Contact mil gaya
        print("Contact Found")

        # Phone number print karo
        print("Phone Number:", contacts[name])

        # Loop turant stop ho jayega
        break

else:
    # Ye else tab chalega jab loop me contact nahi mila
    print("Contact Not Found")