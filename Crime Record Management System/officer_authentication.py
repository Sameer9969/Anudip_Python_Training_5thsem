# Function to login the officer/user
def login(is_login):

    # Check if user is already logged in
    if is_login:
        print("You are already logged in!")
        return True

    # Take email and password from user
    user_mail = input("Enter email: ")
    user_pass = input("Enter password: ")

    try:
        # Open authentication file in read mode
        with open("user_auth.txt", "r") as file:

            # Read the file line by line
            for line in file:

                # Remove newline and split email,password using comma
                data = line.strip().split(",")

                # Store email and password separately
                email = data[0]
                password = data[1]

                # Check if entered credentials match stored credentials
                if user_mail == email and user_pass == password:
                    print("Login Successful!")
                    return True

            # Execute if no matching account is found
            print("Invalid Email or Password!")
            return False

    # Handle error if authentication file does not exist
    except FileNotFoundError:
        print("user_auth.txt not found!")
        return False


# Function to create a new officer account
def create_officer_account(is_login):

    # Prevent account creation if user is already logged in
    if is_login:
        print("You are already logged in!")
        print("Please logout first to create another account.")
        return

    # Take email and password from user
    user_mail = input("Enter Email: ").strip()
    user_pass = input("Enter Password: ").strip()

    # Check if email or password is empty
    if user_mail == "" or user_pass == "":
        print("Email and Password cannot be empty!")
        return

    try:
        # Open authentication file in read mode
        with open("user_auth.txt", "r") as file:

            # Check every existing account
            for line in file:

                # Split email and password
                data = line.strip().split(",")

                # Prevent duplicate account creation
                if user_mail == data[0]:
                    print("Account already exists!")
                    return

    # Ignore error if file does not exist
    except FileNotFoundError:
        pass

    # Open file in append mode to add new account
    with open("user_auth.txt", "a") as file:

        # Save email and password in file
        file.write(f"{user_mail},{user_pass}\n")

    # Display success message
    print("Account Created Successfully!")

    # Update login status
    is_login = True

    # Return updated login status
    return is_login


# Function to change account password
def change_password(is_login):

    # Allow password change only if user is logged in
    if not is_login:
        print("Please login first!")
        return

    # Take required details from user
    user_mail = input("Enter Email: ").strip()
    old_pass = input("Enter Old Password: ").strip()
    new_pass = input("Enter New Password: ").strip()

    # Prevent empty new password
    if new_pass == "":
        print("New password cannot be empty!")
        return

    # Prevent using same password again
    if old_pass == new_pass:
        print("New password cannot be same as old password!")
        return

    try:
        # Read all account records
        with open("user_auth.txt", "r") as file:
            lines = file.readlines()

        # Flag to check whether password is updated
        updated = False

        # Traverse every account
        for i in range(len(lines)):

            # Split email and password
            data = lines[i].strip().split(",")

            # Verify email and old password
            if user_mail == data[0] and old_pass == data[1]:

                # Replace old password with new password
                lines[i] = f"{user_mail},{new_pass}\n"

                # Mark password as updated
                updated = True

                # Stop searching after successful update
                break

        # If password updated successfully
        if updated:

            # Open file in write mode
            with open("user_auth.txt", "w") as file:

                # Write updated records back to file
                file.writelines(lines)

            print("Password Changed Successfully!")

        # Execute if email/password is incorrect
        else:
            print("Invalid Email or Old Password!")

    # Handle error if file does not exist
    except FileNotFoundError:
        print("user_auth.txt not found!")   