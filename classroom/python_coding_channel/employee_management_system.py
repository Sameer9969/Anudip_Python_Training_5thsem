"""Problem 6: Employee Attendance Monitoring System 
Problem Statement 
Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance).  
Sample Output 
Present Employees: 7 
 
Absent Employees: 3 
 
Absent Employee IDs: 
EMP102 
EMP105 
EMP108 
 
Attendance Percentage: 70.0% 
 
Absentee Report Generated Successfully. 
 
Attendance Award Eligibility: 
Not Applicable"""


# Employee Attendance Monitoring System

# Open attendance file in read mode
file = open("attendance.txt", "r")

# Read all lines from file
data = file.readlines()

# Close file
file.close()

# Variables
present = 0
absent = 0
absent_ids = []

# Check attendance of each employee
for line in data:
    emp_id, status = line.strip().split(",")

    if status == "P":
        present += 1
    else:
        absent += 1
        absent_ids.append(emp_id)

# Total employees
total_employees = present + absent

# Attendance percentage
attendance_percentage = (present / total_employees) * 100

# Create absentee report file
report = open("absent_report.txt", "w")

for emp_id in absent_ids:
    report.write(emp_id + "\n")

report.close()

# Display Results
print("Present Employees:", present)

print("\nAbsent Employees:", absent)

print("\nAbsent Employee IDs:")
for emp_id in absent_ids:
    print(emp_id)

print("\nAttendance Percentage:", attendance_percentage, "%")

print("\nAbsentee Report Generated Successfully.")

# Attendance Award Eligibility
print("\nAttendance Award Eligibility:")

# Since only one attendance record is available,
# nobody can be confirmed for 100% attendance
print("Not Applicable")