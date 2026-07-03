def login(is_login):

    if is_login:
        print("You are already logged in!")
        return True

    user_mail = input("Enter email: ")
    user_pass = input("Enter password: ")

    try:
        with open("user_auth.txt", "r") as file:

            for line in file:
                data = line.strip().split(",")

                email = data[0]
                password = data[1]

                if user_mail == email and user_pass == password:
                    print("Login Successful!")
                    return True

            print("Invalid Email or Password!")
            return False

    except FileNotFoundError:
        print("user_auth.txt not found!")
        return False
    

def create_officer_account(is_login):
    if is_login:
        print("You are already logged in!")
        print("Please logout first to create another account.")
        return
    user_mail = input("Enter Email: ").strip()
    user_pass = input("Enter Password: ").strip()

    if user_mail == "" or user_pass == "":
        print("Email and Password cannot be empty!")
        return

    try:
        with open("user_auth.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if user_mail == data[0]:
                    print("Account already exists!")
                    return

    except FileNotFoundError:
        pass

    with open("user_auth.txt", "a") as file:
        file.write(f"{user_mail},{user_pass}\n")

    print("Account Created Successfully!")   
    is_login=True
    return is_login 



def change_password(is_login):

    if not is_login:
        print("Please login first!")
        return

    user_mail = input("Enter Email: ").strip()
    old_pass = input("Enter Old Password: ").strip()
    new_pass = input("Enter New Password: ").strip()

    if new_pass == "":
        print("New password cannot be empty!")
        return

    if old_pass == new_pass:
        print("New password cannot be same as old password!")
        return

    try:
        with open("user_auth.txt", "r") as file:
            lines = file.readlines()

        updated = False

        for i in range(len(lines)):
            data = lines[i].strip().split(",")

            if user_mail == data[0] and old_pass == data[1]:
                lines[i] = f"{user_mail},{new_pass}\n"
                updated = True
                break

        if updated:
            with open("user_auth.txt", "w") as file:
                file.writelines(lines)

            print("Password Changed Successfully!")
        else:
            print("Invalid Email or Old Password!")

    except FileNotFoundError:
        print("user_auth.txt not found!")    