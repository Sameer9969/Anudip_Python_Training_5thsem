def add_criminal():
    cid = input("Enter Criminal ID: ").strip()
    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    crime = input("Enter Crime Type: ").strip()

    try:
        with open("criminals.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if cid == data[0]:
                    print("Criminal ID already exists!")
                    return

    except FileNotFoundError:
        pass

    with open("criminals.txt", "a") as file:
        file.write(f"{cid},{name},{age},{crime}\n")

    print("Criminal Added Successfully!")


def view_criminals():
    try:
        with open("criminals.txt", "r") as file:
            print("\nID\tName\tAge\tCrime")

            for line in file:
                data = line.strip().split(",")

                print(f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}")

    except FileNotFoundError:
        print("No criminal records found!")


def search_criminal():
    cid = input("Enter Criminal ID: ").strip()

    try:
        with open("criminals.txt", "r") as file:

            for line in file:
                data = line.strip().split(",")

                if cid == data[0]:
                    print("\nCriminal Found")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Crime:", data[3])
                    return

            print("Criminal not found!")

    except FileNotFoundError:
        print("No criminal records found!")


def update_criminal():
    cid = input("Enter Criminal ID to Update: ").strip()

    try:
        with open("criminals.txt", "r") as file:
            lines = file.readlines()

        updated = False

        for i in range(len(lines)):
            data = lines[i].strip().split(",")

            if cid == data[0]:

                print("Current Name:", data[1])
                print("Current Age:", data[2])
                print("Current Crime:", data[3])

                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                crime = input("Enter New Crime Type: ")

                lines[i] = f"{cid},{name},{age},{crime}\n"

                updated = True
                break

        if updated:

            with open("criminals.txt", "w") as file:
                file.writelines(lines)

            print("Criminal Updated Successfully!")

        else:
            print("Criminal not found!")

    except FileNotFoundError:
        print("No criminal records found!")


def delete_criminal():
    cid = input("Enter Criminal ID to Delete: ").strip()

    try:
        with open("criminals.txt", "r") as file:
            lines = file.readlines()

        deleted = False
        new_lines = []

        for line in lines:
            data = line.strip().split(",")

            if cid == data[0]:
                deleted = True
            else:
                new_lines.append(line)

        if deleted:

            with open("criminals.txt", "w") as file:
                file.writelines(new_lines)

            print("Criminal Deleted Successfully!")

        else:
            print("Criminal not found!")

    except FileNotFoundError:
        print("No criminal records found!")