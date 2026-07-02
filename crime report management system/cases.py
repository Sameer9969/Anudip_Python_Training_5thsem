# cases.py
# cases.py

# Function to open a new case
def open_case():   # New case create karne ka function

    case_id = input("Enter Case ID: ")   # User se Case ID lena

    status = "Open"   # Naye case ka default status "Open" rakhna

    try:   # Error handle karne ke liye

        file = open("cases.txt", "a")   # cases.txt file Append Mode me kholna

        file.write(case_id + "," + status + "\n")   # Case ID aur status file me save karna

        file.close()   # File close karna

        print("Case Opened Successfully")   # Success message print karna

    except:   # Agar koi bhi error aaye
        print("Error While Opening Case")   # Error message print karna


# Function to view all cases
def view_cases():   # Sabhi cases dekhne ka function

    try:   # Error handle karne ke liye

        file = open("cases.txt", "r")   # File Read Mode me kholna

        print("\n===== CASE LIST =====")   # Heading print karna

        found = False   # Shuru me maan lo koi record nahi mila

        for line in file:   # File ki har line ko padhna

            print(line.strip())   # Newline hata kar record print karna

            found = True   # Agar ek bhi record mila to True kar do

        file.close()   # File close karna

        if found == False:   # Agar koi record nahi mila
            print("No Cases Found")   # Message print karna

    except FileNotFoundError:   # Agar file exist nahi karti

        print("cases.txt File Not Found")   # Error message print karna


# Function to update case status
def update_case_status():   # Kisi case ka status update karne ka function

    case_id = input("Enter Case ID: ")   # User se Case ID lena
    new_status = input("Enter New Status: ")   # User se naya status lena

    records = []   # Saare records temporary list me store honge

    found = False   # Shuru me maan lo Case ID nahi mili

    try:   # Error handle karne ke liye

        file = open("cases.txt", "r")   # File Read Mode me kholna

        for line in file:   # Har line ko padhna

            data = line.strip().split(",")   # Case ID aur Status ko alag karna

            if data[0] == case_id:   # Agar Case ID match ho gayi

                data[1] = new_status   # Status update kar do

                found = True   # Case ID mil gayi

            records.append(data)   # Updated ya old record list me add kar do

        file.close()   # Read wali file close karna

        file = open("cases.txt", "w")   # File Write Mode me kholna (purani file overwrite hogi)

        for record in records:   # List ke har record par loop chalana

            file.write(record[0] + "," + record[1] + "\n")   # Record ko file me dobara likhna

        file.close()   # File close karna

        if found:   # Agar Case ID mil gayi
            print("Status Updated Successfully")   # Success message
        else:   # Agar Case ID nahi mili
            print("Case ID Not Found")   # Error message

    except FileNotFoundError:   # Agar file nahi mili

        print("cases.txt File Not Found")   # Error message


# Function to close a case
def close_case():   # Case ko Close karne ka function

    case_id = input("Enter Case ID: ")   # User se Case ID lena

    records = []   # Saare records temporary list me store honge

    found = False   # Shuru me maan lo Case ID nahi mili

    try:   # Error handle karne ke liye

        file = open("cases.txt", "r")   # File Read Mode me kholna

        for line in file:   # Har line ko padhna

            data = line.strip().split(",")   # Case ID aur Status ko alag karna

            if data[0] == case_id:   # Agar Case ID match ho gayi

                data[1] = "Closed"   # Status ko "Closed" kar do

                found = True   # Case ID mil gayi

            records.append(data)   # Updated ya old record list me list me add karna

        file.close()   # Read wali file close karna

        file = open("cases.txt", "w")   # File Write Mode me kholna

        for record in records:   # List ke har record par loop chalana

            file.write(record[0] + "," + record[1] + "\n")   # Record ko file me dobara save karna

        file.close()   # File close karna

        if found:   # Agar Case ID mil gayi
            print("Case Closed Successfully")   # Success message

        else:   # Agar Case ID nahi mili
            print("Case ID Not Found")   # Error message

    except FileNotFoundError:   # Agar file exist nahi karti

        print("cases.txt File Not Found")   # Error message