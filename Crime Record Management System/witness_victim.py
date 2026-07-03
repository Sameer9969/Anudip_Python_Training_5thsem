def add_victim():

    fir_id = input("Enter FIR ID: ")
    name = input("Victim Name: ")
    contact = input("Contact: ")

    with open("victims.txt", "a") as file:

        file.write(f"{fir_id},Victim,{name},{contact}\n")

    print("Victim Added Successfully!")

def add_witness():

    fir_id = input("Enter FIR ID: ")
    name = input("Witness Name: ")
    contact = input("Contact: ")

    with open("victims.txt", "a") as file:

        file.write(f"{fir_id},Witness,{name},{contact}\n")

    print("Witness Added Successfully!")


def view_victims_witness():

    try:

        with open("victims.txt", "r") as file:

            print("\nFIR ID\tType\tName\tContact")
            print("-" * 45)

            for line in file:

                data = line.strip().split(",")

                print(
                    f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}"
                )

    except FileNotFoundError:

        print("No Records Found!")


def search_vw():

    fir_id = input("Enter FIR ID: ")

    found = False

    try:

        with open("victims.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if fir_id == data[0]:

                    print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]}")
                    found = True

            if not found:
                print("No records found for this FIR!")

    except FileNotFoundError:

        print("No Records Found!")


def delete_vw():

    fir_id = input("Enter FIR ID: ")

    try:

        with open("victims.txt", "r") as file:

            lines = file.readlines()

        new_lines = []
        deleted = False

        for line in lines:

            data = line.strip().split(",")

            if fir_id == data[0]:

                # skip matching record
                deleted = True

            else:

                new_lines.append(line)

        if deleted:

            with open("victims.txt", "w") as file:

                file.writelines(new_lines)

            print("Record Deleted Successfully!")

        else:

            print("No record found!")

    except FileNotFoundError:

        print("No Records Found!")

        
                            
