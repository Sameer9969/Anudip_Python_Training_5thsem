"""5. Daily Expense Tracker and Report Generator 
Problem Statement 
Daily expenses are recorded in expenses.txt. 
File Format 
Food,450 
Travel,300 
Shopping,1200 
Electricity,850 
Internet,700 
Entertainment,600 
Medicine,400 
Education,1500 
Fuel,900 
Miscellaneous,250 
Requirements 
Develop a program to: 
1. Display all expenses.  
2. Calculate total expenditure.  
3. Find the category with highest and lowest spending.  
4. Display expenses greater than ₹800.  
5. Add a new expense category.  
6. Update an existing expense amount.  
7. Generate a summary report in report.txt containing:  
o Total Expenses  
o Highest Expense Category  
o Lowest Expense Category  
o Categories spending more than ₹800 """


# Daily Expense Tracker System

# Expenses store karne ke liye empty list
expenses = []

# expenses.txt file ko read mode me open kar rahe hain
file = open("expenses.txt", "r")

# File ki har line ko read karenge
for line in file:

    # Extra newline remove kar rahe hain
    line = line.strip()

    # Category aur amount ko comma se separate kar rahe hain
    data = line.split(",")

    # Expense category store kar rahe hain
    category = data[0]

    # Amount ko integer me convert kar rahe hain
    amount = int(data[1])

    # List me expense add kar rahe hain
    expenses.append([category, amount])

# File close kar rahe hain
file.close()

# Menu ko repeat karne ke liye loop
while True:

    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Highest and Lowest Spending")
    print("4. Expenses Greater Than ₹800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Report and Exit")

    # User se choice le rahe hain
    choice = int(input("Enter your choice: "))

    # --------------------------------
    # 1. Display All Expenses
    # --------------------------------
    if choice == 1:

        print("\nALL EXPENSES")

        # Sabhi expenses display karenge
        for expense in expenses:
            print(expense[0], "-", expense[1])

    # --------------------------------
    # 2. Calculate Total Expenditure
    # --------------------------------
    elif choice == 2:

        # Total amount store karne ke liye variable
        total = 0

        # Sabhi amounts ko add karenge
        for expense in expenses:
            total = total + expense[1]

        print("Total Expenditure = ₹", total)

    # --------------------------------
    # 3. Highest and Lowest Spending
    # --------------------------------
    elif choice == 3:

        # Pehle expense ko highest maan rahe hain
        highest = expenses[0]

        # Pehle expense ko lowest maan rahe hain
        lowest = expenses[0]

        # List me traverse karenge
        for expense in expenses:

            # Highest expense check kar rahe hain
            if expense[1] > highest[1]:
                highest = expense

            # Lowest expense check kar rahe hain
            if expense[1] < lowest[1]:
                lowest = expense

        print("Highest Spending Category:")
        print(highest[0], "-", highest[1])

        print("Lowest Spending Category:")
        print(lowest[0], "-", lowest[1])

    # --------------------------------
    # 4. Expenses Greater Than ₹800
    # --------------------------------
    elif choice == 4:

        print("\nExpenses Greater Than ₹800")

        # Sabhi expenses check karenge
        for expense in expenses:

            # Agar amount 800 se zyada hai
            if expense[1] > 800:
                print(expense[0], "-", expense[1])

    # --------------------------------
    # 5. Add New Expense Category
    # --------------------------------
    elif choice == 5:

        # Nayi category input
        category = input("Enter Category Name: ")

        # Naya amount input
        amount = int(input("Enter Amount: "))

        # List me add kar rahe hain
        expenses.append([category, amount])

        print("Expense Added Successfully")

    # --------------------------------
    # 6. Update Existing Expense
    # --------------------------------
    elif choice == 6:

        # Jis category ko update karna hai
        update_category = input("Enter Category Name: ")

        found = False

        # Category search karenge
        for expense in expenses:

            if expense[0].lower() == update_category.lower():

                # Naya amount input
                new_amount = int(input("Enter New Amount: "))

                # Amount update kar rahe hain
                expense[1] = new_amount

                print("Expense Updated Successfully")

                found = True
                break

        # Agar category na mile
        if found == False:
            print("Category Not Found")

    # --------------------------------
    # 7. Generate Report and Exit
    # --------------------------------
    elif choice == 7:

        # Total expense calculate kar rahe hain
        total = 0

        for expense in expenses:
            total = total + expense[1]

        # Highest aur lowest find kar rahe hain
        highest = expenses[0]
        lowest = expenses[0]

        for expense in expenses:

            if expense[1] > highest[1]:
                highest = expense

            if expense[1] < lowest[1]:
                lowest = expense

        # report.txt file write mode me open kar rahe hain
        report = open("report.txt", "w")

        # Report file me data write kar rahe hain
        report.write("DAILY EXPENSE REPORT\n")
        report.write("=====================\n\n")

        report.write("Total Expenses = ₹" + str(total) + "\n\n")

        report.write("Highest Expense Category = ")
        report.write(highest[0] + " (₹" + str(highest[1]) + ")\n\n")

        report.write("Lowest Expense Category = ")
        report.write(lowest[0] + " (₹" + str(lowest[1]) + ")\n\n")

        report.write("Categories Spending More Than ₹800\n")

        # ₹800 se zyada expenses report me likhenge
        for expense in expenses:

            if expense[1] > 800:
                report.write(expense[0] + " - ₹" + str(expense[1]) + "\n")

        # File close kar rahe hain
        report.close()

        print("Report Generated Successfully")
        print("Data Saved in report.txt")

        # Program band kar rahe hain
        break

    # --------------------------------
    # Invalid Choice
    # --------------------------------
    else:

        print("Invalid Choice")

        # cd "lab work/function_10june"