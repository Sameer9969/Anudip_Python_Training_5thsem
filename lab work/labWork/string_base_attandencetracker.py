"""8. String-Based Attendance Tracker 
Problem Statement 
Attendance of a student for 15 days is represented as: 
PPAPPPAAPPPPAPP 
Where: 
• P = Present  
• A = Absent  
Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%.  
Sample Output 
Attendance Record: 
PPAPPPAAPPPPAPP 
 
Present Days: 11 
Absent Days: 4 
 
Attendance Percentage: 73.33% 
 
Longest Present Streak: 4 
Longest Absent Streak: 2 
 
Attendance Status: Below 75%"""

#----------------------------------------------
# String-Based Attendance Tracker
#----------------------------------------------

# Attendance record of student
attendance = "PPAPPPAAPPPPAPP"

# Display attendance record
print("Attendance Record:")
print(attendance)

#----------------------------------------------
# 1. Count Present and Absent Days
#----------------------------------------------

present_days = 0
absent_days = 0

# Traverse each character
for ch in attendance:

    # Count Present days
    if ch == "P":
        present_days += 1

    # Count Absent days
    elif ch == "A":
        absent_days += 1

print("\nPresent Days:", present_days)
print("Absent Days:", absent_days)

#----------------------------------------------
# 2. Calculate Attendance Percentage
#----------------------------------------------

# Total days in attendance record
total_days = len(attendance)

# Formula:
# (Present Days / Total Days) × 100
attendance_percentage = (present_days / total_days) * 100

print("\nAttendance Percentage:",
    round(attendance_percentage, 2), "%")

#----------------------------------------------
# 3. Find Longest Consecutive Streak of Presence
#----------------------------------------------

current_present = 0
longest_present = 0

# Traverse attendance record
for ch in attendance:

    # If Present
    if ch == "P":

        # Increase current streak
        current_present += 1

        # Update longest streak if needed
        if current_present > longest_present:
            longest_present = current_present

    else:
        # Reset streak when Absent found
        current_present = 0

print("\nLongest Present Streak:", longest_present)

#----------------------------------------------
# 4. Find Longest Consecutive Streak of Absence
#----------------------------------------------

current_absent = 0
longest_absent = 0

# Traverse attendance record
for ch in attendance:

    # If Absent
    if ch == "A":

        # Increase current streak
        current_absent += 1

        # Update longest streak if needed
        if current_absent > longest_absent:
            longest_absent = current_absent

    else:
        # Reset streak when Present found
        current_absent = 0

print("Longest Absent Streak:", longest_absent)

#----------------------------------------------
# 5. Determine Attendance Status
#----------------------------------------------

# Check if attendance is below 75%
if attendance_percentage < 75:
    print("\nAttendance Status: Below 75%")
else:
    print("\nAttendance Status: Above 75%")