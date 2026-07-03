# Function to add a victim record
def add_victim():

    # Take FIR ID from the user
    fir_id = input("Enter FIR ID: ")

    # Take victim name
    name = input("Victim Name: ")

    # Take victim contact number
    contact = input("Contact: ")

    # Open victims file in append mode
    with open("victims.txt", "a") as file:

        # Store victim details in the file
        file.write(f"{fir_id},Victim,{name},{contact}\n")

    # Display success message
    print("Victim Added Successfully!")


# Function to add a witness record
def add_witness():

    # Take FIR ID from the user
    fir_id = input("Enter FIR ID: ")

    # Take witness name
    name = input("Witness Name: ")

    # Take witness contact number
    contact = input("Contact: ")

    # Open victims file in append mode
    with open("victims.txt", "a") as file:

        # Store witness details in the file
        file.write(f"{fir_id},Witness,{name},{contact}\n")

    # Display success message
    print("Witness Added Successfully!")


# Function to display all victims and witnesses
def view_victims_witness():

    try:

        # Open victims file in read mode
        with open("victims.txt", "r") as file:

            # Display table heading
            print("\nFIR ID\tType\tName\tContact")
            print("-" * 45)

            # Read every record
            for line in file:

                # Split the record into individual fields
                data = line.strip().split(",")

                # Display record in tabular format
                print(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}")

    # Handle missing file error
    except FileNotFoundError:

        print("No Records Found!")


# Function to search victim/witness records using FIR ID
def search_vw():

    # Take FIR ID from the user
    fir_id = input("Enter FIR ID: ")

    # Flag to check whether record exists
    found = False

    try:

        # Open victims file
        with open("victims.txt", "r") as file:

            # Read every record
            for line in file:

                # Split record into fields
                data = line.strip().split(",")

                # Check whether FIR ID matches
                if fir_id == data[0]:

                    # Display matching record
                    print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]}")

                    # Mark record as found
                    found = True

            # Execute if no matching record exists
            if not found:
                print("No records found for this FIR!")

    # Handle missing file error
    except FileNotFoundError:

        print("No Records Found!")


# Function to delete victim/witness records using FIR ID
def delete_vw():

    # Take FIR ID from the user
    fir_id = input("Enter FIR ID: ")

    try:

        # Read all records from the file
        with open("victims.txt", "r") as file:

            lines = file.readlines()

        # List to store remaining records
        new_lines = []

        # Flag to check whether deletion occurs
        deleted = False

        # Traverse every record
        for line in lines:

            # Split record into fields
            data = line.strip().split(",")

            # Check whether FIR ID matches
            if fir_id == data[0]:

                # Skip matching record (delete it)
                deleted = True

            else:

                # Keep non-matching records
                new_lines.append(line)

        # If at least one record was deleted
        if deleted:

            # Open file in write mode
            with open("victims.txt", "w") as file:

                # Write remaining records back to the file
                file.writelines(new_lines)

            # Display success message
            print("Record Deleted Successfully!")

        # Execute if no matching record exists
        else:

            print("No record found!")

    # Handle missing file error
    except FileNotFoundError:

        print("No Records Found!")

        
                            
