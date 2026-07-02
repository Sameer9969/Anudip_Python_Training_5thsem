def open_case():

    case_id = input("Enter Case ID: ")
    fir_id = input("Enter FIR ID: ")

    try:

        # Check duplicate Case ID
        with open("cases.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if case_id == data[0]:
                    print("Case ID already exists!")
                    return

    except FileNotFoundError:
        pass

    # New case starts with Open status
    with open("cases.txt", "a") as file:

        file.write(f"{case_id},{fir_id},Open\n")

    print("Case Opened Successfully!")


def view_cases():

    try:

        with open("cases.txt", "r") as file:

            print("\nCase ID\tFIR ID\tStatus")
            print("-" * 40)

            for line in file:

                data = line.strip().split(",")

                print(
                    f"{data[0]}\t{data[1]}\t{data[2]}"
                )

    except FileNotFoundError:

        print("No Cases Found!")

def search_case():

    case_id = input("Enter Case ID: ")

    try:

        with open("cases.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if case_id == data[0]:

                    print("\nCase Found")
                    print("Case ID :", data[0])
                    print("FIR ID  :", data[1])
                    print("Status  :", data[2])

                    return

            print("Case not found!")

    except FileNotFoundError:

        print("No Cases Found!")

def update_case_status():

    case_id = input("Enter Case ID: ")

    try:

        with open("cases.txt", "r") as file:

            lines = file.readlines()

        found = False

        for i in range(len(lines)):

            data = lines[i].strip().split(",")

            if case_id == data[0]:

                print("\n1. Open")
                print("2. Under Investigation")
                print("3. Evidence Collected")
                print("4. Closed")

                choice = input("Select Status: ")

                if choice == "1":
                    status = "Open"

                elif choice == "2":
                    status = "Under Investigation"

                elif choice == "3":
                    status = "Evidence Collected"

                elif choice == "4":
                    status = "Closed"

                else:
                    print("Invalid Status!")
                    return

                # Update status
                lines[i] = f"{data[0]},{data[1]},{status}\n"

                found = True
                break

        if found:

            with open("cases.txt", "w") as file:
                file.writelines(lines)

            print("Status Updated Successfully!")

        else:
            print("Case not found!")

    except FileNotFoundError:

        print("No Cases Found!")


def delete_case():

    case_id = input("Enter Case ID: ")

    try:

        with open("cases.txt", "r") as file:

            lines = file.readlines()

        new_lines = []
        deleted = False

        for line in lines:

            data = line.strip().split(",")

            if case_id == data[0]:

                # Skip record to delete
                deleted = True

            else:

                new_lines.append(line)

        if deleted:

            with open("cases.txt", "w") as file:

                file.writelines(new_lines)

            print("Case Deleted Successfully!")

        else:

            print("Case not found!")

    except FileNotFoundError:

        print("No Cases Found!")                        