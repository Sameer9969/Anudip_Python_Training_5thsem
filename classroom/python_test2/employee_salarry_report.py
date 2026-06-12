"""Problem 12: Employee Salary Report Generator 
Problem Statement 
Employee details are stored in a text file named employees.txt. 
Sample Input/Data (employees.txt) 
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
Tasks 
1. Display employees earning more than ₹50,000.  
2. Find the highest-paid employee.  
3. Find the lowest-paid employee.  
4. Calculate the average salary.  
5. Generate salary categories:  
o High (≥ ₹60,000)  
o Medium (₹40,000 – ₹59,999)  
o Low (< ₹40,000)  
Sample Output 
Employees Earning Above ₹50,000: 
Rahul 
Neha 
Sneha 
Pooja 
Anjali 
 
Highest Paid Employee: 
Pooja (₹72,000) 
 
Lowest Paid Employee: 
Amit (₹29,000) 
 
Average Salary: ₹50,000 
 
High Salary: 
['Neha', 'Pooja', 'Anjali'] 
 
Medium Salary: 
['Anuj', 'Rahul', 'Sneha', 'Karan'] 
 
Low Salary: 
['Priya', 'Amit', 'Rohit']"""
#
# cd classroom\python_test2
#===========================================
# 1. Display employees earning more than ₹50,000.
#===========================================
print("Employees Earning Above ₹50,000:")
file = open("employees.txt", "r")
for line in file:
    emp_id, name, salary = line.strip().split(",")
    if int(salary) > 50000:
        print(name)
file.close()
#=============================================
# 2. Find the highest-paid employee.
#=============================================

print("Highest Paid Employee:")
highest = 0
file = open("employees.txt", "r")
for line in file:
    emp_id, name, salary = line.strip().split(",")
    if int(salary) > highest:
        highest = int(salary)
        highest_emp = name
file.close()
print(highest_emp, "(", highest, ")")
#===========================================
# 3. Find the lowest-paid employee.
#===========================================
print("Lowest Paid Employee:")
lowest = float('inf')
file = open("employees.txt", "r")
for line in file:
    emp_id, name, salary = line.strip().split(",")
    if int(salary) < lowest:
        lowest = int(salary)
        lowest_emp = name
file.close()
print(lowest_emp, "(", lowest, ")")
#===========================================
# 4. Calculate the average salary.
#===========================================
avg_salary = 0
file = open("employees.txt", "r")
for linr in file:
    avg_salary += int(salary)
avg_salary = avg_salary / len(salary)
print("Average Salary:", avg_salary)

#===========================================
# 5. Generate salary categories:  
# High (≥ ₹60,000)  
# Medium (₹40,000 – ₹59,999)  
# Low (< ₹40,000) 
#===========================================
print("High Salary:")
file = open("employees.txt", "r")
for line in file:
    emp_id, name, salary = line.strip().split(",")
    if int(salary) >= 60000:
        print(name)
file.close()

print("Medium Salary:")
file = open("employees.txt", "r")
for line in file:
    emp_id, name, salary = line.strip().split(",")
    if 40000 <= int(salary) < 60000:
        print(name)
file.close()

print("Low Salary:")
file = open("employees.txt", "r")
for line in file:
    emp_id, name, salary = line.strip().split(",")
    if int(salary) < 40000:
        print(name)
file.close()
#===========================================

