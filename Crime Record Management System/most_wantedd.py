# Function to add a criminal to the Most Wanted list
def add_most_wanted():

    # Take Criminal ID from the user
    criminal_id = input("Enter Criminal ID: ")

    # Take Criminal Name from the user
    name = input("Enter Criminal Name: ")

    # Take Reward Amount from the user
    reward = input("Enter Reward Amount: ")

    try:

        # Open wanted.txt file in read mode
        with open("wanted.txt", "r") as file:

            # Read each record from the file
            for line in file:

                # Remove newline and split record using comma
                data = line.strip().split(",")

                # Check if Criminal ID already exists
                if criminal_id == data[0]:

                    # Display duplicate record message
                    print("Criminal already in Most Wanted List!")

                    # Stop the function
                    return

    # Ignore error if file does not exist
    except FileNotFoundError:
        pass

    # Open file in append mode to add new record
    with open("wanted.txt", "a") as file:

        # Save Criminal ID, Name and Reward into the file
        file.write(
            f"{criminal_id},{name},{reward}\n"
        )

    # Display success message
    print("Added To Most Wanted List Successfully!")


# Function to display all Most Wanted criminals
def view_most_wanted():

    try:

        # Open wanted.txt file in read mode
        with open("wanted.txt", "r") as file:

            # Display table heading
            print("\nCriminal ID\tName\tReward")

            # Display separator line
            print("-" * 40)

            # Read every record from the file
            for line in file:

                # Remove newline and split record
                data = line.strip().split(",")

                # Display criminal details
                print(
                    f"{data[0]}\t{data[1]}\t₹{data[2]}"
                )

    # Handle missing file
    except FileNotFoundError:

        # Display error message
        print("No Most Wanted Records Found!")


# Function to search a Most Wanted criminal
def search_most_wanted():

    # Take Criminal ID from the user
    criminal_id = input("Enter Criminal ID: ")

    try:

        # Open wanted.txt file in read mode
        with open("wanted.txt", "r") as file:

            # Read every record
            for line in file:

                # Split current record
                data = line.strip().split(",")

                # Check whether Criminal ID matches
                if criminal_id == data[0]:

                    # Display search result heading
                    print("\nCriminal Found")

                    # Display Criminal ID
                    print("Criminal ID :", data[0])

                    # Display Criminal Name
                    print("Name :", data[1])

                    # Display Reward Amount
                    print("Reward : ₹", data[2])

                    # Stop searching after finding the record
                    return

            # Display message if Criminal ID is not found
            print("Criminal not found!")

    # Handle missing file
    except FileNotFoundError:

        # Display error message
        print("No Most Wanted Records Found!")


# Function to remove a criminal from the Most Wanted list
def remove_most_wanted():

    # Take Criminal ID from the user
    criminal_id = input("Enter Criminal ID: ")

    try:

        # Open wanted.txt file in read mode
        with open("wanted.txt", "r") as file:

            # Read all records into a list
            lines = file.readlines()

        # Create a new list for remaining records
        new_lines = []

        # Variable to check whether record was removed
        removed = False

        # Read each record
        for line in lines:

            # Split current record
            data = line.strip().split(",")

            # Check if Criminal ID matches
            if criminal_id == data[0]:

                # Mark record as removed
                removed = True

            else:

                # Keep all remaining records
                new_lines.append(line)

        # Check whether deletion was successful
        if removed:

            # Open file in write mode
            with open("wanted.txt", "w") as file:

                # Save updated records
                file.writelines(new_lines)

            # Display success message
            print("Removed Successfully!")

        else:

            # Display message if Criminal ID is not found
            print("Criminal not found!")

    # Handle missing file
    except FileNotFoundError:

        # Display error message
        print("No Most Wanted Records Found!")