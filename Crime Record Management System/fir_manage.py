# Function to register a new FIR
def register_fir():

    # Take FIR ID from the user and remove extra spaces
    fir_id = input("Enter FIR ID: ").strip()

    # Take Criminal ID related to the FIR
    criminal_id = input("Enter Criminal ID: ").strip()

    # Take Crime Type from the user
    crime_type = input("Enter Crime Type: ").strip()

    # Take FIR registration date
    date = input("Enter Date: ").strip()

    try:
        # Open FIR file in read mode to check existing records
        with open("fir.txt", "r") as file:

            # Read every record from the file
            for line in file:

                # Remove newline and split record using comma
                data = line.strip().split(",")

                # Check if FIR ID already exists
                if fir_id == data[0]:
                    print("FIR ID already exists!")
                    return

    # Ignore error if file does not exist
    except FileNotFoundError:
        pass

    # Open file in append mode
    with open("fir.txt", "a") as file:

        # Save FIR details into the file
        file.write(f"{fir_id},{criminal_id},{crime_type},{date}\n")

    # Display success message
    print("FIR Registered Successfully!")


# Function to display all FIR records
def view_firs():

    try:
        # Open FIR file in read mode
        with open("fir.txt", "r") as file:

            # Display table heading
            print("\nFIR ID\tCriminal ID\tCrime\tDate")

            # Read every record
            for line in file:

                # Split record into list
                data = line.strip().split(",")

                # Display FIR details
                print(
                    f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}"
                )

    # Handle missing file
    except FileNotFoundError:
        print("No FIR records found!")


# Function to search an FIR by FIR ID
def search_fir():

    # Take FIR ID from user
    fir_id = input("Enter FIR ID: ").strip()

    try:
        # Open FIR file
        with open("fir.txt", "r") as file:

            # Read every record
            for line in file:

                # Split current record
                data = line.strip().split(",")

                # Check if FIR ID matches
                if fir_id == data[0]:

                    # Display FIR details
                    print("\nFIR Found")
                    print("FIR ID:", data[0])
                    print("Criminal ID:", data[1])
                    print("Crime Type:", data[2])
                    print("Date:", data[3])

                    return

            # Display message if FIR not found
            print("FIR not found!")

    # Handle missing file
    except FileNotFoundError:
        print("No FIR records found!")


# Function to update an existing FIR
def update_fir():

    # Take FIR ID from the user
    fir_id = input("Enter FIR ID: ").strip()

    try:
        # Read all FIR records
        with open("fir.txt", "r") as file:
            lines = file.readlines()

        # Variable to check successful update
        updated = False

        # Traverse every record
        for i in range(len(lines)):

            # Split current record
            data = lines[i].strip().split(",")

            # Check matching FIR ID
            if fir_id == data[0]:

                # Take updated Criminal ID
                criminal_id = input("Enter New Criminal ID: ")

                # Take updated Crime Type
                crime_type = input("Enter New Crime Type: ")

                # Take updated Date
                date = input("Enter New Date: ")

                # Replace old record with updated values
                lines[i] = (
                    f"{fir_id},{criminal_id},"
                    f"{crime_type},{date}\n"
                )

                # Mark record as updated
                updated = True
                break

        # If update is successful
        if updated:

            # Open file in write mode
            with open("fir.txt", "w") as file:

                # Save updated records
                file.writelines(lines)

            # Display success message
            print("FIR Updated Successfully!")

        # If FIR ID not found
        else:
            print("FIR not found!")

    # Handle missing file
    except FileNotFoundError:
        print("No FIR records found!")


# Function to delete an FIR record
def delete_fir():

    # Take FIR ID from the user
    fir_id = input("Enter FIR ID: ").strip()

    try:
        # Read all FIR records
        with open("fir.txt", "r") as file:
            lines = file.readlines()

        # List to store remaining records
        new_lines = []

        # Variable to check successful deletion
        deleted = False

        # Traverse every record
        for line in lines:

            # Split current record
            data = line.strip().split(",")

            # Check matching FIR ID
            if fir_id == data[0]:

                # Skip this record to delete it
                deleted = True

            else:

                # Keep remaining records
                new_lines.append(line)

        # If deletion is successful
        if deleted:

            # Open file in write mode
            with open("fir.txt", "w") as file:

                # Save remaining records
                file.writelines(new_lines)

            # Display success message
            print("FIR Deleted Successfully!")

        # If FIR ID is not found
        else:
            print("FIR not found!")

    # Handle missing file
    except FileNotFoundError:
        print("No FIR records found!")