# Function to add a new criminal record
def add_criminal():

    # Take Criminal ID from the user and remove extra spaces
    cid = input("Enter Criminal ID: ").strip()

    # Take Criminal Name from the user
    name = input("Enter Name: ").strip()

    # Take Criminal Age from the user
    age = input("Enter Age: ").strip()

    # Take Crime Type from the user
    crime = input("Enter Crime Type: ").strip()

    try:
        # Open the criminals file in read mode
        with open("criminals.txt", "r") as file:

            # Read each record from the file
            for line in file:

                # Remove newline and split the record using comma
                data = line.strip().split(",")

                # Check if Criminal ID already exists
                if cid == data[0]:
                    print("Criminal ID already exists!")
                    return

    # Ignore the error if the file does not exist
    except FileNotFoundError:
        pass

    # Open file in append mode to add new record
    with open("criminals.txt", "a") as file:

        # Store Criminal ID, Name, Age and Crime Type
        file.write(f"{cid},{name},{age},{crime}\n")

    # Display success message
    print("Criminal Added Successfully!")


# Function to display all criminal records
def view_criminals():

    try:
        # Open the file in read mode
        with open("criminals.txt", "r") as file:

            # Display table heading
            print("\nID\tName\tAge\tCrime")

            # Read every record
            for line in file:

                # Split record into list
                data = line.strip().split(",")

                # Display criminal details
                print(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}")

    # Handle missing file
    except FileNotFoundError:
        print("No criminal records found!")


# Function to search a criminal using Criminal ID
def search_criminal():

    # Take Criminal ID from user
    cid = input("Enter Criminal ID: ").strip()

    try:
        # Open the file
        with open("criminals.txt", "r") as file:

            # Read every record
            for line in file:

                # Split current record
                data = line.strip().split(",")

                # Check if Criminal ID matches
                if cid == data[0]:

                    # Display criminal details
                    print("\nCriminal Found")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Crime:", data[3])

                    return

            # Display message if record not found
            print("Criminal not found!")

    # Handle missing file
    except FileNotFoundError:
        print("No criminal records found!")


# Function to update an existing criminal record
def update_criminal():

    # Take Criminal ID to update
    cid = input("Enter Criminal ID to Update: ").strip()

    try:
        # Read all records from the file
        with open("criminals.txt", "r") as file:
            lines = file.readlines()

        # Variable to check successful update
        updated = False

        # Traverse all records
        for i in range(len(lines)):

            # Split current record
            data = lines[i].strip().split(",")

            # Check matching Criminal ID
            if cid == data[0]:

                # Display current details
                print("Current Name:", data[1])
                print("Current Age:", data[2])
                print("Current Crime:", data[3])

                # Take updated details
                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                crime = input("Enter New Crime Type: ")

                # Replace old record with updated values
                lines[i] = f"{cid},{name},{age},{crime}\n"

                # Mark record as updated
                updated = True
                break

        # Save changes if update is successful
        if updated:

            # Open file in write mode
            with open("criminals.txt", "w") as file:

                # Write updated records
                file.writelines(lines)

            # Display success message
            print("Criminal Updated Successfully!")

        # If Criminal ID not found
        else:
            print("Criminal not found!")

    # Handle missing file
    except FileNotFoundError:
        print("No criminal records found!")


# Function to delete a criminal record
def delete_criminal():

    # Take Criminal ID from user
    cid = input("Enter Criminal ID to Delete: ").strip()

    try:
        # Read all records from file
        with open("criminals.txt", "r") as file:
            lines = file.readlines()

        # Variable to check successful deletion
        deleted = False

        # List to store remaining records
        new_lines = []

        # Traverse every record
        for line in lines:

            # Split current record
            data = line.strip().split(",")

            # Check matching Criminal ID
            if cid == data[0]:

                # Skip this record to delete it
                deleted = True

            else:

                # Keep remaining records
                new_lines.append(line)

        # If record deleted successfully
        if deleted:

            # Open file in write mode
            with open("criminals.txt", "w") as file:

                # Save remaining records
                file.writelines(new_lines)

            # Display success message
            print("Criminal Deleted Successfully!")

        # If Criminal ID not found
        else:
            print("Criminal not found!")

    # Handle missing file
    except FileNotFoundError:
        print("No criminal records found!")