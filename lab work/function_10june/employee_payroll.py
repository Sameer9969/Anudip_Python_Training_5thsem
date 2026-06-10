"""1. Employee Payroll Management System 
Problem Statement 
A company stores employee details in a text file named employees.txt. 
File Format 
EMP101,Anuj,45000 
EMP102,Rahul,52000 
EMP103,Priya,38000 
EMP104,Neha,61000 
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP107,Karan,47000 
EMP108,Pooja,72000 
EMP109,Rohit,33000 
EMP110,Anjali,68000 
Requirements 
Create a menu-driven program to: 
1. Display all employee records.  
2. Search employee details using Employee ID.  
3. Calculate the average salary.  
4. Find the highest-paid and lowest-paid employee.  
5. Display employees earning above ₹50,000.  
6. Add a new employee record to the file.  
7. Generate salary categories:  
o High (₹60,000 and above)  
o Medium (₹40,000–₹59,999)  
o Low (Below ₹40,000)  
"""
# Employee Payroll Management System

while True:

    # Display Menu
    print("\n===== Employee Payroll Management System =====")
    print("1. Display All Employees")
    print("2. Search Employee by ID")
    print("3. Calculate Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Earning Above 50000")
    print("6. Add New Employee")
    print("7. Salary Categories")
    print("8. Exit")

    # Take choice from user
    choice = int(input("Enter your choice: "))

    # ==========================================
    # Option 1 : Display All Employee Records
    # ==========================================
    if choice == 1:

        # Open file in read mode
        file = open('employees.txt', 'r')

        print("\nEmployee Records:")

        # Read and display each line
        for line in file:
            print(line.strip())

        # Close file
        file.close()

    # ==========================================
    # Option 2 : Search Employee by ID
    # ==========================================
    elif choice == 2:

        # Take employee id from user
        emp_id = input("Enter Employee ID: ")

        # Open file
        file = open('employees.txt', 'r')

        # Variable to check employee found or not
        found = False

        # Read file line by line
        for line in file:

            # Split data using comma
            data = line.strip().split(",")

            # Check employee id
            if data[0] == emp_id:

                print("\nEmployee Found")
                print("ID :", data[0])
                print("Name :", data[1])
                print("Salary :", data[2])

                found = True

        # If employee not found
        if found == False:
            print("Employee Not Found")

        # Close file
        file.close()

    # ==========================================
    # Option 3 : Calculate Average Salary
    # ==========================================
    elif choice == 3:

        # Open file
        file = open('employees.txt', 'r')

        total_salary = 0
        count = 0

        # Read each record
        for line in file:

            data = line.strip().split(",")

            # Add salary to total
            total_salary = total_salary + int(data[2])

            # Count employees
            count = count + 1

        # Calculate average
        average = total_salary / count

        print("Average Salary =", average)

        # Close file
        file.close()

    # ==========================================
    # Option 4 : Highest and Lowest Paid Employee
    # ==========================================
    elif choice == 4:

        # Open file
        file = open('employees.txt', 'r')

        highest_salary = 0
        lowest_salary = 999999

        highest_name = ""
        lowest_name = ""

        # Read records
        for line in file:

            data = line.strip().split(",")

            salary = int(data[2])

            # Check highest salary
            if salary > highest_salary:
                highest_salary = salary
                highest_name = data[1]

            # Check lowest salary
            if salary < lowest_salary:
                lowest_salary = salary
                lowest_name = data[1]

        print("\nHighest Paid Employee")
        print(highest_name, "-", highest_salary)

        print("\nLowest Paid Employee")
        print(lowest_name, "-", lowest_salary)

        # Close file
        file.close()

    # ==========================================
    # Option 5 : Employees Earning Above 50000
    # ==========================================
    elif choice == 5:

        # Open file
        file = open('employees.txt', 'r')

        print("\nEmployees Earning Above 50000")

        # Read records
        for line in file:

            data = line.strip().split(",")

            # Check salary greater than 50000
            if int(data[2]) > 50000:
                print(data[0], data[1], data[2])

        # Close file
        file.close()

    # ==========================================
    # Option 6 : Add New Employee
    # ==========================================
    elif choice == 6:

        # Take employee details
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        # Open file in append mode
        file = open('employees.txt', 'a')

        # Add new record
        file.write("\n" + emp_id + "," + name + "," + salary)

        # Close file
        file.close()

        print("Employee Added Successfully")

    # ==========================================
    # Option 7 : Salary Categories
    # ==========================================
    elif choice == 7:

        # Open file
        file = open('employees.txt', 'r')

        print("\nSalary Categories")

        # Read records
        for line in file:

            data = line.strip().split(",")

            salary = int(data[2])

            # High Salary
            if salary >= 60000:
                print(data[1], "-", salary, "- High")

            # Medium Salary
            elif salary >= 40000:
                print(data[1], "-", salary, "- Medium")

            # Low Salary
            else:
                print(data[1], "-", salary, "- Low")

        # Close file
        file.close()

    # ==========================================
    # Option 8 : Exit Program
    # ==========================================
    elif choice == 8:

        print("Program Ended")
        break

    # Invalid Choice
    else:
        print("Invalid Choice")