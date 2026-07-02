# Import all functions related to Officer Authentication
from officer_authentication import *

# Import all functions related to Criminal Management
from criminal_management import *

# Import all functions related to FIR Management
from fir_manage import *

# Import all functions related to Case Tracking
from case_track import *

# Import all functions related to Search & Filter
from search_filters import *

# Import all functions related to Reports & Statistics
from report_statis import *

# Import all functions related to Evidence Management
from evidence_manage import *

# Import all functions related to Most Wanted Criminals
from most_wantedd import *

# Import all functions related to Victim & Witness Management
from witness_victim import *

# Import all functions related to Backup & Recovery
from recovery_backup import *


# Function to display the Officer Authentication menu
def officer_authentication(is_login):

    # Run the menu continuously until the user selects Back
    while True:

        # Display Officer Authentication menu title
        print("\n===== OFFICER AUTHENTICATION =====")

        # Display Login option
        print("1. Login")

        # Display Create Officer Account option
        print("2. Create Officer Account")

        # Display Change Password option
        print("3. Change Password")

        # Display Logout option
        print("4. Logout")

        # Display Back option
        print("5. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Login the officer
            if choice == 1:
                is_login = login(is_login)

            # Create a new officer account
            elif choice == 2:
                create_officer_account(is_login)

            # Change officer password
            elif choice == 3:
                change_password(is_login)

            # Logout current officer
            elif choice == 4:

                # Check whether any officer is logged in
                if is_login:

                    # Change login status to False
                    is_login = False

                    # Display successful logout message
                    print("Logged Out Successfully!")

                else:

                    # Display message if no officer is logged in
                    print("No user is currently logged in.")

            # Return to Main Menu
            elif choice == 5:

                # Inform user
                print("Returning to Main Menu...")

                # Return updated login status
                return is_login

            # Invalid menu option
            else:

                # Ask user to enter a valid option
                print("Enter a number between 1 and 5.")

        # Handle invalid input such as letters
        except ValueError:

            # Display error message
            print("Please enter a valid number.")


# Function to display Criminal Management menu
def criminal_management():

    # Keep displaying menu until user chooses Back
    while True:

        # Display menu heading
        print("\n===== CRIMINAL RECORD MANAGEMENT =====")

        # Display Add Criminal option
        print("1. Add Criminal")

        # Display View Criminals option
        print("2. View Criminals")

        # Display Search Criminal option
        print("3. Search Criminal")

        # Display Update Criminal option
        print("4. Update Criminal")

        # Display Delete Criminal option
        print("5. Delete Criminal")

        # Display Back option
        print("6. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Call Add Criminal function
            if choice == 1:
                add_criminal()

            # Call View Criminals function
            elif choice == 2:
                view_criminals()

            # Call Search Criminal function
            elif choice == 3:
                search_criminal()

            # Call Update Criminal function
            elif choice == 4:
                update_criminal()

            # Call Delete Criminal function
            elif choice == 5:
                delete_criminal()

            # Return to Main Menu
            elif choice == 6:

                # Display message
                print("Returning to Main Menu...")

                # Exit loop
                break

            # Invalid menu option
            else:
                print("Enter a number between 1 and 6.")

        # Handle invalid input
        except ValueError:
            print("Please enter a valid number.")


# Function to display FIR Management menu
def fir_management(is_login):

    # Keep showing menu until user selects Back
    while True:

        # Display menu heading
        print("\n===== FIR MANAGEMENT =====")

        # Display Register FIR option
        print("1. Register FIR")

        # Display View FIRs option
        print("2. View FIRs")

        # Display Search FIR option
        print("3. Search FIR")

        # Display Update FIR option
        print("4. Update FIR")

        # Display Delete FIR option
        print("5. Delete FIR")

        # Display Back option
        print("6. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Register a new FIR
            if choice == 1:
                register_fir()

            # View all FIR records
            elif choice == 2:
                view_firs()

            # Search FIR by ID
            elif choice == 3:
                search_fir()

            # Update FIR details
            elif choice == 4:
                update_fir()

            # Delete FIR record
            elif choice == 5:
                delete_fir()

            # Exit FIR menu
            elif choice == 6:
                break

            # Invalid option
            else:
                print("Enter a number between 1 and 6.")

        # Handle invalid input
        except ValueError:
            print("Invalid Input!")


# Function to display Case Tracking menu
def case_tracking():

    # Keep displaying menu until Back is selected
    while True:

        # Display menu heading
        print("\n===== CASE TRACKING =====")

        # Display Open Case option
        print("1. Open Case")

        # Display View Cases option
        print("2. View Cases")

        # Display Search Case option
        print("3. Search Case")

        # Display Update Status option
        print("4. Update Status")

        # Display Delete Case option
        print("5. Delete Case")

        # Display Back option
        print("6. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Open a new case
            if choice == 1:
                open_case()

            # View all cases
            elif choice == 2:
                view_cases()

            # Search a case
            elif choice == 3:
                search_case()

            # Update case status
            elif choice == 4:
                update_case_status()

            # Delete a case
            elif choice == 5:
                delete_case()

            # Exit menu
            elif choice == 6:
                break

            # Invalid menu choice
            else:
                print("Enter a number between 1 and 6.")

        # Handle invalid input
        except ValueError:
            print("Invalid Input!")


# Function to display Search & Filter menu
def search_filter():

    # Keep displaying menu until Back is selected
    while True:

        # Display menu heading
        print("\n===== SEARCH & FILTER =====")

        # Search Criminal using Criminal ID
        print("1. Search Criminal By ID")

        # Search Criminal using Name
        print("2. Search Criminal By Name")

        # Search FIR using FIR ID
        print("3. Search FIR By FIR ID")

        # Search FIR using Criminal ID
        print("4. Search FIR By Criminal ID")

        # Search Case using Case ID
        print("5. Search Case By Case ID")

        # Search Case using Status
        print("6. Search Case By Status")

        # Return to Main Menu
        print("7. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Search Criminal by ID
            if choice == 1:
                search_criminal_id()

            # Search Criminal by Name
            elif choice == 2:
                search_criminal_name()

            # Search FIR by FIR ID
            elif choice == 3:
                search_fir_id()

            # Search FIR using Criminal ID
            elif choice == 4:
                search_fir_criminal()
                        # Search Case using Case ID
            elif choice == 5:
                search_case_id()

            # Search Case using Status
            elif choice == 6:
                search_case_status()

            # Exit Search & Filter menu
            elif choice == 7:
                break

            # Display message for invalid menu choice
            else:
                print("Enter number between 1 and 7.")

        # Handle invalid input such as letters
        except ValueError:
            print("Invalid Input!")


# Function to display Reports & Statistics menu
def reports_statistics():

    # Keep displaying menu until user selects Back
    while True:

        # Display menu heading
        print("\n===== REPORTS & STATISTICS =====")

        # Display option to view total criminals
        print("1. Total Criminals")

        # Display option to view total FIRs
        print("2. Total FIRs")

        # Display option to view total cases
        print("3. Total Cases")

        # Display option to view open cases
        print("4. Open Cases")

        # Display option to view closed cases
        print("5. Closed Cases")

        # Display option to view crime-wise statistics
        print("6. Crime Wise Statistics")

        # Display Back option
        print("7. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Display total number of criminals
            if choice == 1:
                total_criminals()

            # Display total number of FIRs
            elif choice == 2:
                total_firs()

            # Display total number of cases
            elif choice == 3:
                total_cases()

            # Display all open cases
            elif choice == 4:
                open_cases()

            # Display all closed cases
            elif choice == 5:
                closed_cases()

            # Display crime-wise statistics
            elif choice == 6:
                crime_statistics()

            # Exit Reports menu
            elif choice == 7:
                break

            # Display message for invalid option
            else:
                print("Enter number between 1 and 7.")

        # Handle invalid input
        except ValueError:
            print("Invalid Input!")


# Function to display Evidence Management menu
def evidence_management():

    # Keep displaying menu until user selects Back
    while True:

        # Display menu heading
        print("\n===== EVIDENCE MANAGEMENT =====")

        # Display option to add evidence
        print("1. Add Evidence")

        # Display option to view all evidence
        print("2. View Evidence")

        # Display option to search evidence
        print("3. Search Evidence")

        # Display option to delete evidence
        print("4. Delete Evidence")

        # Display Back option
        print("5. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Add new evidence record
            if choice == 1:
                add_evidence()

            # View all evidence records
            elif choice == 2:
                view_evidence()

            # Search evidence by Evidence ID
            elif choice == 3:
                search_evidence()

            # Delete evidence record
            elif choice == 4:
                delete_evidence()

            # Exit Evidence Management menu
            elif choice == 5:
                break

            # Display message for invalid option
            else:
                print("Enter number between 1 and 5.")

        # Handle invalid input
        except ValueError:
            print("Invalid Input!")


# Function to display Most Wanted Criminal menu
def most_wanted():

    # Keep displaying menu until user selects Back
    while True:

        # Display menu heading
        print("\n===== MOST WANTED CRIMINALS =====")

        # Display option to add a criminal to Most Wanted list
        print("1. Add To Most Wanted")

        # Display option to view Most Wanted list
        print("2. View Most Wanted List")

        # Display option to search a Most Wanted criminal
        print("3. Search Criminal")

        # Display option to remove a criminal from the list
        print("4. Remove Criminal")

        # Display Back option
        print("5. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Add criminal to Most Wanted list
            if choice == 1:
                add_most_wanted()

            # View all Most Wanted criminals
            elif choice == 2:
                view_most_wanted()

            # Search a Most Wanted criminal
            elif choice == 3:
                search_most_wanted()

            # Remove a criminal from Most Wanted list
            elif choice == 4:
                remove_most_wanted()

            # Exit Most Wanted menu
            elif choice == 5:
                break

            # Display message for invalid option
            else:
                print("Enter number between 1 and 5.")

        # Handle invalid input
        except ValueError:
            print("Invalid Input!")


# Function to display Victim & Witness Management menu
def victim_witness():

    # Keep displaying menu until user selects Back
    # Keep displaying the Victim & Witness menu until the user selects Back
    while True:

    # Display Victim & Witness module heading
        print("\n===== VICTIM & WITNESS MODULE =====")

    # Display Add Victim option
        print("1. Add Victim")

    # Display Add Witness option
        print("2. Add Witness")

    # Display View Records option
        print("3. View Records")

    # Display Search by FIR ID option
        print("4. Search by FIR ID")

    # Display Delete Record option
        print("5. Delete Record")

    # Display Back option
        print("6. Back")

        try:

        # Take user's menu choice
            choice = int(input("Enter Choice: "))

        # Add a new victim record
            if choice == 1:
                add_victim()

        # Add a new witness record
            elif choice == 2:
                add_witness()

        # Display all victim and witness records
            elif choice == 3:
                view_victims_witness()

        # Search records using FIR ID
            elif choice == 4:
                search_vw()

        # Delete a victim or witness record
            elif choice == 5:
                delete_vw()

        # Exit Victim & Witness menu
            elif choice == 6:
                break

        # Display message for invalid option
            else:
                print("Enter number between 1 and 6.")

    # Handle invalid input such as letters
        except ValueError:
            print("Invalid Input!")


# Function to display Backup & Recovery menu
def backup_recovery():

    # Keep displaying menu until user selects Back
    while True:

        # Display Backup & Recovery heading
        print("\n===== BACKUP & RECOVERY =====")

        # Display Create Backup option
        print("1. Create Backup")

        # Display Restore Backup option
        print("2. Restore Backup")

        # Display Back option
        print("3. Back")

        try:

            # Take user's menu choice
            choice = int(input("Enter Choice: "))

            # Create backup of project files
            if choice == 1:
                create_backup()

            # Restore backup files
            elif choice == 2:
                restore_backup()

            # Exit Backup menu
            elif choice == 3:
                break

            # Invalid menu option
            else:
                print("Enter number between 1 and 3.")

        # Handle invalid input
        except ValueError:
            print("Invalid Input!")


# Function to display project dashboard
def dashboard():

    # Display dashboard heading
    print("\n=================================")
    print("        POLICE DASHBOARD")
    print("=================================")

    try:

        # Read criminal records file
        with open("criminals.txt", "r") as file:

            # Count total criminals
            criminals = len(file.readlines())

    # If file is missing, set count to zero
    except:
        criminals = 0

    try:

        # Read FIR file
        with open("fir.txt", "r") as file:

            # Count total FIR records
            firs = len(file.readlines())

    # If file is missing
    except:
        firs = 0

    try:

        # Read all case records
        with open("cases.txt", "r") as file:
            cases = file.readlines()

        # Count total cases
        total_cases = len(cases)

        # Initialize open case counter
        open_cases = 0

        # Initialize closed case counter
        closed_cases = 0

        # Traverse every case record
        for line in cases:

            # Split current record
            data = line.strip().split(",")

            # Check if case is Open
            if data[2] == "Open":
                open_cases += 1

            # Check if case is Closed
            elif data[2] == "Closed":
                closed_cases += 1

    # If file is missing
    except:
        total_cases = 0
        open_cases = 0
        closed_cases = 0

    try:

        # Dictionary to store crime frequencies
        crime_count = {}

        # Read criminal records
        with open("criminals.txt", "r") as file:

            # Traverse every record
            for line in file:

                # Split record into list
                data = line.strip().split(",")

                # Get crime type
                crime = data[3]

                # Increase count if already exists
                if crime in crime_count:
                    crime_count[crime] += 1

                # Otherwise create new entry
                else:
                    crime_count[crime] = 1

        # Check whether any crime exists
        if crime_count:

            # Find most common crime
            most_common_crime = max(crime_count, key=crime_count.get)

        # No records found
        else:
            most_common_crime = "N/A"

    # Handle missing file
    except:
        most_common_crime = "N/A"

    # Display dashboard statistics
    print(f"Total Criminals : {criminals}")

    # Display total FIRs
    print(f"Total FIRs      : {firs}")

    # Display total cases
    print(f"Total Cases     : {total_cases}")

    # Display open cases
    print(f"Open Cases      : {open_cases}")

    # Display closed cases
    print(f"Closed Cases    : {closed_cases}")

    # Display most common crime type
    print(f"Most Crime Type : {most_common_crime}")

    # Display ending line
    print("=================================\n")


# Initially no officer is logged in
is_login = False

# Keep displaying the main menu until Exit is selected
while True:

    # Display system heading
    print("\n===== CRIME RECORD MANAGEMENT SYSTEM =====")

    # Display current login status
    print(f"Login Status: {'Logged In' if is_login else 'Not Logged In'}")

    # Display Main Menu options
    print("1. Officer Authentication")
    print("2. Criminal Record Management")
    print("3. FIR Registration")
    print("4. Case Tracking")
    print("5. Search & Filter")
    print("6. Reports & Statistics")
    print("7. Evidence Management")
    print("8. Most Wanted Criminals")
    print("9. Victim & Witness Records")
    print("10. Backup & Recovery")
    print("11. Dashboard")
    print("12. Exit")

    # Take user's menu choice
    choice = input("Enter choice: ")

    # Open Officer Authentication module
    if choice == "1":
        is_login = officer_authentication(is_login)

    # Open Criminal Management after login
    elif choice == "2":

        # Check login status
        if is_login:
            criminal_management()

        # Ask user to login first
        else:
            print("Please login first!")

    # Open FIR Management after login
    elif choice == "3":

        if is_login:
            fir_management()

        else:
            print("Please login first!")

    # Open Case Tracking after login
    elif choice == "4":

        if is_login:
            case_tracking()

        else:
            print("Please login first!")

    # Open Search & Filter module after login
    elif choice == "5":

        if is_login:
            search_filter()

        else:
            print("Please login first!")

    # Open Reports module after login
    elif choice == "6":

        if is_login:
            reports_statistics()

        else:
            print("Please login first!")

    # Open Evidence Management after login
    elif choice == "7":

        if is_login:
            evidence_management()

        else:
            print("Please login first!")

    # Open Most Wanted module after login
    elif choice == "8":

        if is_login:
            most_wanted()

        else:
            print("Please login first!")

    # Open Victim & Witness module after login
    elif choice == "9":

        if is_login:
            victim_witness()

        else:
            print("Please login first!")

    # Open Backup & Recovery module after login
    elif choice == "10":

        if is_login:
            backup_recovery()

        else:
            print("Please login first!")

    # Open Dashboard after login
    elif choice == "11":

        if is_login:
            dashboard()

        else:
            print("Please login first!")

    # Exit the application
    elif choice == "12":

        # Display exit message
        print("Exiting...")

        # Stop the program
        break

    # Display message for invalid menu choice
    else:
        print("Invalid Choice!")