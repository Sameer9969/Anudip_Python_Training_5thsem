"""Create Attendance tracker of 30 students. Ask the user to input roll number of student and also 
input whether student is Present or Absent. Store the data in dictionary where roll number will 
be used as a key and Attendance as Value. 
Display the roll number of students who are Present"""


attendance = {}

# Input attendance of 30 students
for i in range(1, 5):
    roll_no = int(input("Enter Roll Number: "))
    status = input("Present or Absent (P/A): ")

    attendance[roll_no] = status

# Display present students
print("\nStudents who are Present:")

for roll_no in attendance:
    if attendance[roll_no] == "P" or attendance[roll_no] == "p":
        print(roll_no)
  