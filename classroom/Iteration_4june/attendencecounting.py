# a teacher recording the attendence of strenght of class ic 30 every time 
#every time they need to insert the student is present or absent so count the total number of student is present or absent

#--------------------------------
student = 1
present_count = 0
absent_count = 0

while student <= 30:
    attendance = input("Is student present or absent? (P/A): ")

    if attendance == 'P' or attendance == 'p':
        print("Student", student, "is present.")
        present_count += 1

    elif attendance == 'A' or attendance == 'a':
        print("Student", student, "is absent.")
        absent_count += 1

    else:
        print("Invalid input. Please enter 'P' or 'A'.")
        continue

    student += 1
    print("-------------------")

print("\nAttendance Summary")
print("Total Present Students:", present_count)
print("Total Absent Students:", absent_count)
print("--------------------------------")

