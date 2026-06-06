"""Problem Statement 
Employee data is stored as tuples: 
employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 
Write a program to: 
• Display employees earning above ₹50,000.  
• Find the highest-paid employee.  
• Calculate total salary expenditure.  
• Count employees earning below ₹40,000. """

employees = [ 
    ("Rahul", 35000), 
    ("Priya", 55000), 
    ("Amit", 42000), 
    ("Neha", 65000) 
] 

# Display employees earning above ₹50,000
print("Employees Earning Above ₹50,000:")
for employee in employees:
    if employee[1] > 50000:
        print(employee[0])

# Find the highest-paid employee.
highest_paid = employees[0]

for employee in employees:
    if employee[1] > highest_paid[1]:
        highest_paid = employee

print("\nHighest-Paid Employee:")
print(highest_paid[0])

# Calculate total salary expenditure.
total_salary = 0
for employee in employees:
    total_salary += employee[1]

print("\nTotal Salary Expenditure:", total_salary)

# Count employees earning below ₹40,000
count = 0
for employee in employees:
    if employee[1] < 40000:
        count += 1

print("\nEmployees Earning Below ₹40,000:", count)

