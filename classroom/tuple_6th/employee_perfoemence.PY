# Problem Statement 
# A company stores employee details in a tuple. Each employee record contains: 
# employees = ( 
#     ("E101", "Anuj", 92), 
#     ("E102", "Rahul", 76), 
#     ("E103", "Priya", 58), 
#     ("E104", "Neha", 88), 
#     ("E105", "Amit", 45) 
# ) 
# Where: 
# • First value = Employee ID  
# • Second value = Employee Name  
# • Third value = Performance Score  
# Tasks 
# Write a Python program to: 
# 1. Display details of employees scoring 80 or above.  
# 2. Count the number of employees who need improvement (score below 60).  
# 3. Find the employee with the highest score.  
# 4. Create a list containing the names of all employees scoring above 75.  
# 5. Display the performance category for each employee:  
# o 90 and above → Excellent  
# o 75 to 89 → Good  
# o 60 to 74 → Average  
# o Below 60 → Needs Improvement 

#------------------------------------
employees = ( 
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
) 
# 1. Display details of employees scoring 80 or above.
print("Employees Scoring 80 or Above: ")
for i in employees:
    if( i[2] >= 80):
        print(i[0],i[1],i[2])
print("--------------------------------")
# 2. Count the number of employees who need improvement (score below 60).  
count = 0
for emp in employees:
    if(emp[2] <= 60):
        count += 1
print("Employees Needing Improvement: ",count)
print("--------------------------------")
# 3. Find the employee with the highest score.
highest = employees[0]

for emp in employees:
    if emp[2] > highest[2]:
        highest = emp

print("\nHighest Performer:")
print(highest[0], highest[1], highest[2])
print("--------------------------------")
# 4. Create a list containing the names of all employees scoring above 75.  
high_performence = []

for emp in employees:
    if(emp[2] > 75):
        high_performence.append(emp[1])
print("High Performers: ",high_performence)
print("--------------------------------")
# 5. Display the performance category for each employee:  
# o 90 and above → Excellent  
# o 75 to 89 → Good  
# o 60 to 74 → Average  
# o Below 60 → Needs Improvement

print("Performance Categories:")
for emp in employees:
    score = emp[2]

    
    if (score >= 90):
        category = "Excellent"
    elif (score >= 75):
        category = "Good"
    elif (score >= 60):
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)
print("--------------------------------")
