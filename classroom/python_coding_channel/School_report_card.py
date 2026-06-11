"""Problem 4: School Report Card Generator 
Problem Statement 
Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 
1. Calculate grades for all students.  
Passed Students: 9 
Failed Students: 1 
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90).  
Sample Output 
Topper: 
Sneha (95) 

Merit Certificate Holders: 
Anuj 
Sneha 
Anjali 

Report Cards Generated Successfully."""



#==========================================
# School Report Card Generator
#================================

file = open("marks.txt", "r")
students = file.readlines()
file.close()
#=============================================

while True:
    print("\n===== School Report Card Generator =====")
    print("1. Calculate grades for all students.")
    print("2. Generate a report card file report_card.txt.  ")
    print("3. Display topper details.")
    print("4. Count pass and fail students.")
    print("5. Display students eligible for merit certificates (marks ≥ 90).")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    #=============================================
    # 1. Calculate grades for all students.
    #=============================================
    if choice == 1:
        for i, student in enumerate(students):
            data = student.strip().split(",")
            marks = int(data[2])

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 40:
                grade = "D"
            else:
                grade = "F"

            data.append(grade)
            students[i] = ",".join(data)

        print("\nGrades calculated successfully.")
#==================================================
# 2. Generate a report card file report_card.txt.
#==================================================
    elif choice == 2:
        file = open("report_card.txt", "w")

        for student in students:
            data = student.strip().split(",")
            name = data[1]
            marks = int(data[2])
            grade = data[3]

            file.write(f"{name} - {marks} - {grade}\n")

        file.close()

        print("\nReport cards generated successfully.")
#==================================================
# 3. Display topper details.
#==================================================
    elif choice == 3:
        max_marks = 0
        topper = ""

        for student in students:
            data = student.strip().split(",")
            marks = int(data[2])

            if marks > max_marks:
                max_marks = marks
                topper = data[1]


        print(f"\nTopper: {topper} ({max_marks})")
#===================================================
# 4. Count pass and fail students.
#===================================================
    elif choice == 4:
        pass_count = 0
        fail_count = 0

        for student in students:
            data = student.strip().split(",")
            marks = int(data[2])

            if marks >= 40:
                pass_count += 1
            else:
                fail_count += 1

        print(f"\nPassed Students: {pass_count}")
        print(f"Failed Students: {fail_count}")
#===================================================
# 5. Display students eligible for merit certificates (marks ≥ 90). 
#===================================================
    elif choice == 5:
        print("\nMerit Certificate Holders:")

        for student in students:
            data = student.strip().split(",")
            marks = int(data[2])

            if marks >= 90:
                print(data[1])

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
#===================================================