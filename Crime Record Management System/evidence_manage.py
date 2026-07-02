# Function to add a new evidence record
def add_evidence():

    # Take Case ID from the user
    case_id = input("Enter Case ID: ")

    # Take Evidence ID from the user
    evidence_id = input("Enter Evidence ID: ")

    # Take evidence description from the user
    description = input("Enter Evidence Description: ")

    try:

        # Open evidence file in read mode
        with open("evidence.txt", "r") as file:

            # Read every record from the file
            for line in file:

                # Remove newline and split data using comma
                data = line.strip().split(",")

                # Check if Evidence ID already exists
                if evidence_id == data[1]:

                    print("Evidence ID already exists!")
                    return

    # Ignore the error if the file does not exist
    except FileNotFoundError:
        pass

    # Open file in append mode to add new evidence
    with open("evidence.txt", "a") as file:

        # Store Case ID, Evidence ID and Description
        file.write(
            f"{case_id},{evidence_id},{description}\n"
        )

    # Display success message
    print("Evidence Added Successfully!")


# Function to display all evidence records
def view_evidence():

    try:

        # Open evidence file in read mode
        with open("evidence.txt", "r") as file:

            # Display table heading
            print("\nCase ID\tEvidence ID\tDescription")
            print("-" * 50)

            # Read every record
            for line in file:

                # Split record into list
                data = line.strip().split(",")

                # Display evidence details
                print(
                    f"{data[0]}\t{data[1]}\t{data[2]}"
                )

    # Handle missing file
    except FileNotFoundError:

        print("No Evidence Records Found!")


# Function to search evidence by Evidence ID
def search_evidence():

    # Take Evidence ID from user
    evidence_id = input("Enter Evidence ID: ")

    try:

        # Open evidence file
        with open("evidence.txt", "r") as file:

            # Read every record
            for line in file:

                # Split current record
                data = line.strip().split(",")

                # Check if Evidence ID matches
                if evidence_id == data[1]:

                    # Display evidence details
                    print("\nEvidence Found")
                    print("Case ID :", data[0])
                    print("Evidence ID :", data[1])
                    print("Description :", data[2])

                    return

            # Display message if record not found
            print("Evidence not found!")

    # Handle missing file
    except FileNotFoundError:

        print("No Evidence Records Found!")


# Function to delete an evidence record
def delete_evidence():

    # Take Evidence ID from the user
    evidence_id = input("Enter Evidence ID: ")

    try:

        # Read all evidence records
        with open("evidence.txt", "r") as file:

            lines = file.readlines()

        # List to store remaining records
        new_lines = []

        # Variable to check successful deletion
        deleted = False

        # Traverse every record
        for line in lines:

            # Split current record
            data = line.strip().split(",")

            # Check matching Evidence ID
            if evidence_id == data[1]:

                # Skip this record to delete it
                deleted = True

            else:

                # Keep remaining records
                new_lines.append(line)

        # If deletion is successful
        if deleted:

            # Open file in write mode
            with open("evidence.txt", "w") as file:

                # Save remaining records
                file.writelines(new_lines)

            # Display success message
            print("Evidence Deleted Successfully!")

        # If Evidence ID is not found
        else:

            print("Evidence not found!")

    # Handle missing file
    except FileNotFoundError:

        print("No Evidence Records Found!")