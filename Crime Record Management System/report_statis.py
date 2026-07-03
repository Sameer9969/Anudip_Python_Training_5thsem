# Function to count the total number of criminals
def total_criminals():

    try:

        # Open the criminals record file in read mode
        with open("criminals.txt", "r") as file:

            # Count the total number of lines (records)
            count = len(file.readlines())

            # Display the total number of criminals
            print("Total Criminals :", count)

    # Handle error if file does not exist
    except FileNotFoundError:

        print("No Criminal Records Found!")


# Function to count the total number of FIR records
def total_firs():

    try:

        # Open the FIR file
        with open("fir.txt", "r") as file:

            # Count total FIR records
            count = len(file.readlines())

            # Display total FIR count
            print("Total FIRs :", count)

    # Handle missing file error
    except FileNotFoundError:

        print("No FIR Records Found!")


# Function to count the total number of cases
def total_cases():

    try:

        # Open the cases file
        with open("cases.txt", "r") as file:

            # Count total case records
            count = len(file.readlines())

            # Display total cases
            print("Total Cases :", count)

    # Handle missing file error
    except FileNotFoundError:

        print("No Case Records Found!")


# Function to count all open cases
def open_cases():

    # Initialize counter for open cases
    count = 0

    try:

        # Open the cases file
        with open("cases.txt", "r") as file:

            # Read file line by line
            for line in file:

                # Split record using comma
                data = line.strip().split(",")

                # Check if case status is Open
                if data[2] == "Open":

                    # Increase open case count
                    count += 1

        # Display total open cases
        print("Open Cases :", count)

    # Handle missing file error
    except FileNotFoundError:

        print("No Case Records Found!")


# Function to count all closed cases
def closed_cases():

    # Initialize counter for closed cases
    count = 0

    try:

        # Open the cases file
        with open("cases.txt", "r") as file:

            # Read each case record
            for line in file:

                # Split the record into fields
                data = line.strip().split(",")

                # Check if case status is Closed
                if data[2] == "Closed":

                    # Increase closed case count
                    count += 1

        # Display total closed cases
        print("Closed Cases :", count)

    # Handle missing file error
    except FileNotFoundError:

        print("No Case Records Found!")


# Function to generate crime statistics
def crime_statistics():

    # Dictionary to store crime type and its frequency
    crime_count = {}

    try:

        # Open the criminals record file
        with open("criminals.txt", "r") as file:

            # Read every criminal record
            for line in file:

                # Split record into individual fields
                data = line.strip().split(",")

                # Extract crime type (4th column)
                crime = data[3]

                # Check if crime type already exists in dictionary
                if crime in crime_count:

                    # Increase frequency by one
                    crime_count[crime] += 1

                else:

                    # Add new crime type with initial count
                    crime_count[crime] = 1

        # Display heading
        print("\nCrime Statistics")

        # Display each crime type with its total count
        for crime, count in crime_count.items():

            print(f"{crime} : {count}")

    # Handle missing file error
    except FileNotFoundError:

        print("No Criminal Records Found!")