"""Problem 18: Student Attendance Percentage Calculator 
Problem Statement 
The attendance status of a student for 15 days is represented as follows: 
Sample Data 
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P') 
Tasks 
1. Count present days.  
2. Count absent days.  
3. Calculate attendance percentage.  
4. Determine whether attendance is below 75%.  
5. Display the attendance status.  
Sample Output 
Present Days: 11 
 
Absent Days: 4 
 
Attendance Percentage: 73.33% 
 
Attendance Status: 
Below 75%"""

attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P')

# Count Present Days
present = 0
for day in attendance:
    if day == 'P':
        present = present + 1

# Count Absent Days
absent = 0
for day in attendance:
    if day == 'A':
        absent = absent + 1

# Calculate Attendance Percentage
total_days = len(attendance)
percentage = (present / total_days) * 100

# Display Results
print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", round(percentage, 2), "%")

# Check Attendance Status
print("\nAttendance Status:")
if percentage < 75:
    print("Below 75%")
else:
    print("75% or Above")
