# authentication.py
# Login Function
def login():  # Login function banaya gaya

    username = input("Enter Username: ")   # User se username lena
    password = input("Enter Password: ")   # User se password lena

    found = False   # Shuru me maan lo username/password nahi mila

    try:   # Error handle karne ke liye

        file = open("officers.txt", "r")   # officers.txt file Read Mode me kholna

        for line in file:   # File ki har line ko ek-ek karke padhna

            data = line.strip().split(",")   # Newline hatana aur comma ke basis par data alag karna

            if data[0] == username and data[1] == password:   # Username aur password match karna
                found = True   # Agar match ho gaya to found True kar do
                break   # Match mil gaya to loop band kar do

        file.close()   # File close kar do

        if found:   # Agar username/password mil gaya
            print("Login Successful")   # Success message print karo
        else:   # Agar username/password nahi mila
            print("Invalid Username or Password")   # Error message print karo

    except FileNotFoundError:   # Agar file exist nahi karti
        print("officers.txt file not found")   # Error message print karo


# Create Account Function
def create_account():   # Naya account banane ka function

    username = input("Enter Username: ")   # User se username lena
    password = input("Enter Password: ")   # User se password lena

    try:   # Error handle karne ke liye

        file = open("officers.txt", "a")   # File Append Mode me kholna

        file.write(username + "," + password + "\n")   # Username aur password file me save karna

        file.close()   # File close karna

        print("Account Created Successfully")   # Success message

    except:   # Agar koi bhi error aaye
        print("Error Creating Account")   # Error message


# View Accounts Function
def view_accounts():   # Sabhi accounts dekhne ka function

    try:   # Error handle karne ke liye

        file = open("officers.txt", "r")   # File Read Mode me kholna

        print("\nOfficer List")   # Heading print karna

        for line in file:   # File ki har line padhna
            print(line.strip())   # Newline hata kar line print karna

        file.close()   # File close karna

    except FileNotFoundError:   # Agar file nahi mili
        print("No Records Found")   # Error message


# Change Password Function
def change_password():   # Password change karne ka function

    username = input("Enter Username: ")   # User se username lena
    new_password = input("Enter New Password: ")   # User se naya password lena

    records = []   # Saare records temporarily list me store honge
    found = False   # Shuru me maan lo username nahi mila

    try:

        file = open("officers.txt", "r")   # File Read Mode me kholna

        for line in file:   # Har line ko padhna

            data = line.strip().split(",")   # Username aur password ko alag karna

            if data[0] == username:   # Agar username match ho gaya

                data[1] = new_password   # Password replace kar do
                found = True   # Username mil gaya

            records.append(data)   # Updated ya old record list me add karo

        file.close()   # Read wali file close karo

        file = open("officers.txt", "w")   # File Write Mode me kholna (purani file overwrite hogi)

        for record in records:   # List ke har record par loop chalana
            file.write(record[0] + "," + record[1] + "\n")   # Har record ko file me dobara likhna

        file.close()   # File close karna

        if found:   # Agar username mil gaya
            print("Password Changed Successfully")   # Success message
        else:   # Agar username nahi mila
            print("Username Not Found")   # Error message

    except FileNotFoundError:   # Agar file exist nahi karti
        print("File Not Found")   # Error message