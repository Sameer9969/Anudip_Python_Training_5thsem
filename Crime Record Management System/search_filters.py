# Function to search a criminal using Criminal ID
def search_criminal_id():

    # Take Criminal ID from the user
    cid = input("Enter Criminal ID: ")

    try:

        # Open the criminals record file
        with open("criminals.txt", "r") as file:

            # Read each record one by one
            for line in file:

                # Split the record into individual fields
                data = line.strip().split(",")

                # Check whether the entered ID matches the stored ID
                if cid == data[0]:

                    # Display the criminal details
                    print("\nRecord Found")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Crime:", data[3])

                    # Stop searching after finding the record
                    return

            # Execute if no matching record is found
            print("Criminal not found!")

    # Handle missing file error
    except FileNotFoundError:
        print("criminals.txt not found!")


# Function to search criminals by name
def search_criminal_name():

    # Take criminal name and convert it to lowercase
    name = input("Enter Name: ").lower()

    # Flag to track whether a record is found
    found = False

    try:

        # Open the criminals file
        with open("criminals.txt", "r") as file:

            # Read each criminal record
            for line in file:

                # Split the record into fields
                data = line.strip().split(",")

                # Perform case-insensitive partial name search
                if name in data[1].lower():

                    # Display matching criminal record
                    print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]}")

                    # Mark record as found
                    found = True

            # Execute if no matching records exist
            if not found:
                print("No matching records found!")

    # Handle missing file error
    except FileNotFoundError:
        print("criminals.txt not found!")


# Function to search FIR using FIR ID
def search_fir_id():

    # Take FIR ID from user
    fir_id = input("Enter FIR ID: ")

    try:

        # Open the FIR file
        with open("fir.txt", "r") as file:

            # Read every FIR record
            for line in file:

                # Split the record into fields
                data = line.strip().split(",")

                # Check if FIR ID matches
                if fir_id == data[0]:

                    # Display FIR details
                    print("\nFIR Found")
                    print("FIR ID :", data[0])
                    print("Criminal ID :", data[1])
                    print("Crime :", data[2])
                    print("Date :", data[3])

                    # Stop searching after match
                    return

            # Execute if FIR is not found
            print("FIR not found!")

    # Handle missing file error
    except FileNotFoundError:
        print("fir.txt not found!")


# Function to search FIR records using Criminal ID
def search_fir_criminal():

    # Take Criminal ID from user
    cid = input("Enter Criminal ID: ")

    # Flag to track search result
    found = False

    try:

        # Open FIR file
        with open("fir.txt", "r") as file:

            # Read every FIR record
            for line in file:

                # Split the record into fields
                data = line.strip().split(",")

                # Check whether Criminal ID matches
                if cid == data[1]:

                    # Display matching FIR record
                    print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]}")

                    # Mark record as found
                    found = True

            # Execute if no FIR matches the Criminal ID
            if not found:
                print("No FIR found!")

    # Handle missing file error
    except FileNotFoundError:
        print("fir.txt not found!")


# Function to search a case using Case ID
def search_case_id():

    # Take Case ID from user
    case_id = input("Enter Case ID: ")

    try:

        # Open the cases file
        with open("cases.txt", "r") as file:

            # Read every case record
            for line in file:

                # Split record into fields
                data = line.strip().split(",")

                # Check whether Case ID matches
                if case_id == data[0]:

                    # Display case details
                    print("\nCase Found")
                    print("Case ID :", data[0])
                    print("FIR ID :", data[1])
                    print("Status :", data[2])

                    # Stop searching after successful match
                    return

            # Execute if case is not found
            print("Case not found!")

    # Handle missing file error
    except FileNotFoundError:
        print("cases.txt not found!")


# Function to search cases based on their status
def search_case_status():

    # Take status from user and convert to lowercase
    status = input("Enter Status: ").lower()

    # Flag to check whether matching cases exist
    found = False

    try:

        # Open the cases file
        with open("cases.txt", "r") as file:

            # Read every case record
            for line in file:

                # Split record into fields
                data = line.strip().split(",")

                # Compare entered status with stored status
                if status == data[2].lower():

                    # Display matching case
                    print(f"{data[0]} | {data[1]} | {data[2]}")

                    # Mark record as found
                    found = True

            # Execute if no case matches the given status
            if not found:
                print("No case found!")

    # Handle missing file error
    except FileNotFoundError:
        print("cases.txt not found!")