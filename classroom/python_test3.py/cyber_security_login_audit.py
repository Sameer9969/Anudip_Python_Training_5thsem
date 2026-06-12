"""Problem 1: Cyber Security Login Audit System
Problem Statement
A file named login_logs.txt contains user login attempts in the following format:
username,status
anuj,Success
rahul,Failed
anuj,Failed
priya,Failed
rahul,Failed
neha,Success
anuj,Failed
karan,Failed
rahul,Success
priya,Failed
Tasks
1. Count successful and failed login attempts.
2. Identify users with more than 2 failed attempts.
3. Create a dictionary storing the number of failures per user.
4. Create a set of users who logged in successfully.
5. Display users whose accounts should be reviewed.
Sample Output
Successful Login Attempts: 3
Failed Login Attempts: 7

Failure Count per User:
anuj : 2
rahul : 2
priya : 2
karan : 1

Users with Successful Logins:
{'anuj', 'neha', 'rahul'}

Accounts Requiring Review:
None"""

# Define the main function for the login audit program

def login_audit():
    # Start error handling so the program can handle missing files safely
    try:
        # Open the log file in read mode
        file = open("login_logs.txt", "r")

        # Set counters for successful and failed attempts to zero
        success_count = 0
        failed_count = 0

        # Create a dictionary to store failure counts for each user
        failure_dict = {}
        # Create a set to store users who logged in successfully
        success_users = set()

        # Read each line from the file one by one
        for line in file:
            # Remove spaces and extra blank characters from the line
            line = line.strip()

            # Skip the header line of the file
            if line == "username,status":
                continue

            # Split each record into username and status
            username, status = line.split(",")

            # If login was successful, count it and add the user to the set
            if status == "Success":
                success_count += 1
                success_users.add(username)

            # If login failed, count it and update the fail count for that user
            elif status == "Failed":
                failed_count += 1

                # Increase the failure count for an existing user
                if username in failure_dict:
                    failure_dict[username] += 1
                # Create a new entry if the user appears for the first time
                else:
                    failure_dict[username] = 1

        # Close the file after reading all records
        file.close()

        # Print the total number of successful login attempts
        print("Successful Login Attempts:", success_count)
        # Print the total number of failed login attempts
        print("Failed Login Attempts:", failed_count)

        # Display the failure counts for each user
        print("\nFailure Count per User:")
        for user in failure_dict:
            print(user, ":", failure_dict[user])

        # Display the set of users who had at least one successful login
        print("\nUsers with Successful Logins:")
        print(success_users)

        # Check which users need account review because they failed more than twice
        print("\nAccounts Requiring Review:")

        # Assume no user needs review at first
        review_found = False
        for user in failure_dict:
            if failure_dict[user] > 2:
                print(user)
                review_found = True

        # If no user failed more than twice, print None
        if review_found == False:
            print("None")

    # Handle the case where the input file does not exist
    except FileNotFoundError:
        print("login_logs.txt file not found.")
    # Handle any other unexpected errors
    except Exception as e:
        print("Error:", e)


# Call the main function to run the program
login_audit()
