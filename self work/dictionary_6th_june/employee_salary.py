"""3. Employee Salary Processing 
Sample Data 
salary = { 
    "EMP101": 45000, 
    "EMP102": 62000, 
    "EMP103": 38000, 
    "EMP104": 75000, 
    "EMP105": 54000, 
    "EMP106": 29000, 
    "EMP107": 82000, 
    "EMP108": 48000, 
    "EMP109": 36000, 
    "EMP110": 68000 
} 
Tasks 
• Display employees earning above ₹60,000.  
• Count employees earning below ₹40,000.  
• Find the highest-paid employee.  
• Create a list of employees eligible for a bonus (salary > ₹50,000).  
• Calculate the average salary. """

# Employee salary dictionary
# Key = Employee ID
# Value = Salary
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# ==================================================
# 1. Display employees earning above ₹60,000
# ==================================================

print("Employees earning above ₹60,000:")

# Loop through each employee and salary
for emp_id, emp_salary in salary.items():

    # Check if salary is greater than 60000
    if emp_salary > 60000:

        # Print employee ID
        print(emp_id)

# ==================================================
# 2. Count employees earning below ₹40,000
# ==================================================

# Variable to store count
count = 0

# Loop through all salary values
for emp_salary in salary.values():

    # Check if salary is less than 40000
    if emp_salary < 40000:

        # Increase count by 1
        count += 1

# Display total count
print("Employees earning below ₹40,000:", count)

# ==================================================
# 3. Find the highest-paid employee
# ==================================================

# Variable to store highest employee ID
highest_employee = ""

# Variable to store highest salary
# Initially 0 so any salary will be greater than it
highest_salary = 0

# Loop through each employee and salary
for emp_id, emp_salary in salary.items():

    # Check if current salary is greater than highest salary
    if emp_salary > highest_salary:

        # Update highest salary
        highest_salary = emp_salary

        # Store employee ID
        highest_employee = emp_id

# Display highest paid employee
print("Highest Paid Employee:", highest_employee)

# Display highest salary
print("Salary:", highest_salary)

# ==================================================
# 4. Create a list of employees eligible for bonus
# ==================================================

# Empty list to store eligible employees
bonus_list = []

# Loop through each employee and salary
for emp_id, emp_salary in salary.items():

    # Check if salary is greater than 50000
    if emp_salary > 50000:

        # Add employee ID into list
        bonus_list.append(emp_id)

# Display bonus eligible employees
print("Employees eligible for bonus:", bonus_list)

# ==================================================
# 5. Calculate the average salary
# ==================================================

# Variable to store total salary
total_salary = 0

# Loop through all salary values
for emp_salary in salary.values():

    # Add each salary to total
    total_salary += emp_salary

# Total number of employees
total_employees = len(salary)

# Formula:
# Average = Total Salary / Number of Employees
average_salary = total_salary / total_employees

# Display average salary
print("Average Salary:", average_salary)# Employee salary dictionary
# Key = Employee ID
# Value = Salary
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# ==================================================
# 1. Display employees earning above ₹60,000
# ==================================================

print("Employees earning above ₹60,000:")

# Loop through each employee and salary
for emp_id, emp_salary in salary.items():

    # Check if salary is greater than 60000
    if emp_salary > 60000:

        # Print employee ID
        print(emp_id)

# ==================================================
# 2. Count employees earning below ₹40,000
# ==================================================

# Variable to store count
count = 0

# Loop through all salary values
for emp_salary in salary.values():

    # Check if salary is less than 40000
    if emp_salary < 40000:

        # Increase count by 1
        count += 1

# Display total count
print("Employees earning below ₹40,000:", count)

# ==================================================
# 3. Find the highest-paid employee
# ==================================================

# Variable to store highest employee ID
highest_employee = ""

# Variable to store highest salary
# Initially 0 so any salary will be greater than it
highest_salary = 0

# Loop through each employee and salary
for emp_id, emp_salary in salary.items():

    # Check if current salary is greater than highest salary
    if emp_salary > highest_salary:

        # Update highest salary
        highest_salary = emp_salary

        # Store employee ID
        highest_employee = emp_id

# Display highest paid employee
print("Highest Paid Employee:", highest_employee)

# Display highest salary
print("Salary:", highest_salary)

# ==================================================
# 4. Create a list of employees eligible for bonus
# ==================================================

# Empty list to store eligible employees
bonus_list = []

# Loop through each employee and salary
for emp_id, emp_salary in salary.items():

    # Check if salary is greater than 50000
    if emp_salary > 50000:

        # Add employee ID into list
        bonus_list.append(emp_id)

# Display bonus eligible employees
print("Employees eligible for bonus:", bonus_list)

# ==================================================
# 5. Calculate the average salary
# ==================================================

# Variable to store total salary
total_salary = 0

# Loop through all salary values
for emp_salary in salary.values():

    # Add each salary to total
    total_salary += emp_salary

# Total number of employees
total_employees = len(salary)

# Formula:
# Average = Total Salary / Number of Employees
average_salary = total_salary / total_employees

# Display average salary
print("Average Salary:", average_salary)