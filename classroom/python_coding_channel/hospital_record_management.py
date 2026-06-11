"""Problem 2: Hospital Patient Record Management System 
Problem Statement 
A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 
1. Display all patient records.  
2. Display critical patients.  
3. Count patients under each status.  
4. Search patient details using Patient ID.  
5. Save critical patient records to critical_patients.txt.  
Sample Output 
Critical Patients: 
Rahul 
Neha 
Karan 
 
Patient Count: 
Normal : 3 
Stable : 4 
Critical : 3 
 
Patient Found: 
P104,Neha,Critical 
 
Critical Patient Report Generated Successfully."""

#==================================================

# Hospital Patient Record Management System

file = open("patients.txt", "r")
patients = file.readlines()
file.close()

while True:
    print("\n===== Hospital Patient Record Management =====")
    print("1. Display All Patient Records")
    print("2. Display Critical Patients")
    print("3. Count Patients Under Each Status")
    print("4. Search Patient by ID")
    print("5. Save Critical Patients to File")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all records
    if choice == 1:
        print("\nAll Patient Records:")
        for patient in patients:
            print(patient.strip())

    # 2. Display critical patients
    elif choice == 2:
        print("\nCritical Patients:")
        for patient in patients:
            data = patient.strip().split(",")

            if data[2] == "Critical":
                print(data[1])

    # 3. Count patients under each status
    elif choice == 3:
        normal = 0
        stable = 0
        critical = 0

        for patient in patients:
            data = patient.strip().split(",")

            if data[2] == "Normal":
                normal += 1
            elif data[2] == "Stable":
                stable += 1
            elif data[2] == "Critical":
                critical += 1

        print("\nPatient Count:")
        print("Normal :", normal)
        print("Stable :", stable)
        print("Critical :", critical)

    # 4. Search patient by ID
    elif choice == 4:
        pid = input("Enter Patient ID: ")

        found = False

        for patient in patients:
            data = patient.strip().split(",")

            if data[0] == pid:
                print("\nPatient Found:")
                print(patient.strip())
                found = True
                break

        if found == False:
            print("Patient Not Found")

    # 5. Save critical patients to file
    elif choice == 5:
        file = open("critical_patients.txt", "w")

        for patient in patients:
            data = patient.strip().split(",")

            if data[2] == "Critical":
                file.write(patient)

        file.close()

        print("Critical Patient Report Generated Successfully.")

    # 6. Exit
    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")