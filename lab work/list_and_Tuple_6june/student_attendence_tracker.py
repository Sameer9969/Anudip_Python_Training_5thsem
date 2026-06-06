"""Problem Statement 
Attendance for 15 days is recorded as: 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
Write a program to: 
• Count present and absent days.  
• Calculate attendance percentage.  
• Determine eligibility (minimum 75% attendance).  
• Display positions where the student was absent. """
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = 0
absent = 0

# Count Present and Absent
for day in attendance:
    if day == 'P':
        present += 1
    else:
        absent += 1

print("Present Days:", present)
print("Absent Days:", absent)

# Attendance Percentage
percentage = (present / len(attendance)) * 100

print("Attendance Percentage:", percentage)

# Eligibility Check
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Display Absent Positions
print("Absent on Days:")

day_number = 1

for day in attendance:
    if day == 'A':
        print(day_number)

    day_number += 1