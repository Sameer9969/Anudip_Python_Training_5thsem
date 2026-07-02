# Function to open (create) a new case
def open_case():

    # Take Case ID from the user
    case_id = input("Enter Case ID: ")

    # Take related FIR ID from the user
    fir_id = input("Enter FIR ID: ")

    try:

        # Open the cases file in read mode to check existing records
        with open("cases.txt", "r") as file:

            # Read each line from the file
            for line in file:

                # Remove newline and split data using comma
                data = line.strip().split(",")

                # Check if entered Case ID already exists
                if case_id == data[0]:
                    print("Case ID already exists!")
                    return

    # If file does not exist, ignore the error
    except FileNotFoundError:
        pass

    # Open file in append mode to add new case
    with open("cases.txt", "a") as file:

        # Save Case ID, FIR ID and default status (Open)
        file.write(f"{case_id},{fir_id},Open\n")

    # Display success message
    print("Case Opened Successfully!")


# Function to display all cases
def view_cases():

    try:

        # Open cases file in read mode
        with open("cases.txt", "r") as file:

            # Display table heading
            print("\nCase ID\tFIR ID\tStatus")
            print("-" * 40)

            # Read each record from file
            for line in file:

                # Remove newline and split record
                data = line.strip().split(",")

                # Display Case ID, FIR ID and Status
                print(
                    f"{data[0]}\t{data[1]}\t{data[2]}"
                )

    # If file is not found
    except FileNotFoundError:

        print("No Cases Found!")


# Function to search a case using Case ID
def search_case():

    # Take Case ID from user
    case_id = input("Enter Case ID: ")

    try:

        # Open cases file
        with open("cases.txt", "r") as file:

            # Read every record
            for line in file:

                # Split record into list
                data = line.strip().split(",")

                # Check if entered Case ID matches
                if case_id == data[0]:

                    # Display case details
                    print("\nCase Found")
                    print("Case ID :", data[0])
                    print("FIR ID  :", data[1])
                    print("Status  :", data[2])

                    return

            # If no matching case found
            print("Case not found!")

    # Handle missing file
    except FileNotFoundError:

        print("No Cases Found!")


# Function to update case status
def update_case_status():

    # Take Case ID from user
    case_id = input("Enter Case ID: ")

    try:

        # Open file in read mode
        with open("cases.txt", "r") as file:

            # Store all records in a list
            lines = file.readlines()

        # Variable to check whether case exists
        found = False

        # Traverse every record
        for i in range(len(lines)):

            # Split current record
            data = lines[i].strip().split(",")

            # Check matching Case ID
            if case_id == data[0]:

                # Display available status options
                print("\n1. Open")
                print("2. Under Investigation")
                print("3. Evidence Collected")
                print("4. Closed")

                # Take user's choice
                choice = input("Select Status: ")

                # Assign status according to choice
                if choice == "1":
                    status = "Open"

                elif choice == "2":
                    status = "Under Investigation"

                elif choice == "3":
                    status = "Evidence Collected"

                elif choice == "4":
                    status = "Closed"

                # Invalid option entered
                else:
                    print("Invalid Status!")
                    return

                # Replace old record with updated status
                lines[i] = f"{data[0]},{data[1]},{status}\n"

                # Mark record as found
                found = True
                break

        # If record was updated
        if found:

            # Open file in write mode
            with open("cases.txt", "w") as file:

                # Save updated records
                file.writelines(lines)

            # Display success message
            print("Status Updated Successfully!")

        # If Case ID not found
        else:
            print("Case not found!")

    # Handle missing file
    except FileNotFoundError:

        print("No Cases Found!")


# Function to delete a case record
def delete_case():

    # Take Case ID from user
    case_id = input("Enter Case ID: ")

    try:

        # Open file in read mode
        with open("cases.txt", "r") as file:

            # Read all records
            lines = file.readlines()

        # List to store remaining records
        new_lines = []

        # Variable to check deletion
        deleted = False

        # Traverse every record
        for line in lines:

            # Split current record
            data = line.strip().split(",")

            # Check matching Case ID
            if case_id == data[0]:

                # Skip this record to delete it
                deleted = True

            else:

                # Keep all other records
                new_lines.append(line)

        # If record deleted successfully
        if deleted:

            # Open file in write mode
            with open("cases.txt", "w") as file:

                # Save remaining records
                file.writelines(new_lines)

            # Display success message
            print("Case Deleted Successfully!")

        # If Case ID not found
        else:

            print("Case not found!")

    # Handle missing file
    except FileNotFoundError:

        print("No Cases Found!")                        