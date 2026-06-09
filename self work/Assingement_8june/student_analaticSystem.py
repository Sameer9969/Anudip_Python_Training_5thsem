"""1. Student Performance Analytics System 
Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary. 
Example Structure 
students = { 
    "S101": {"name": "Anuj", "marks": 85}, 
    "S102": {"name": "Rahul", "marks": 72} 
} 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85).  
Expected Learning 
• Nested Dictionaries  
• Dictionary Traversal  
• Searching  
• Aggregation  
• Report Generation """

# ==========================================
# STUDENT PERFORMANCE ANALYTICS SYSTEM
# ==========================================

# Nested Dictionary
students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 93},
    "S104": {"name": "Amit", "marks": 45},
    "S105": {"name": "Sneha", "marks": 78},
    "S106": {"name": "Vikram", "marks": 62},
    "S107": {"name": "Neha", "marks": 89},
    "S108": {"name": "Rohan", "marks": 33},
    "S109": {"name": "Karan", "marks": 95},
    "S110": {"name": "Diya", "marks": 55},
    "S111": {"name": "Arjun", "marks": 81},
    "S112": {"name": "Pooja", "marks": 49},
    "S113": {"name": "Deepak", "marks": 67},
    "S114": {"name": "Sonia", "marks": 74},
    "S115": {"name": "Aman", "marks": 91},
    "S116": {"name": "Ritu", "marks": 58},
    "S117": {"name": "Manish", "marks": 76},
    "S118": {"name": "Kavita", "marks": 83},
    "S119": {"name": "Raj", "marks": 40},
    "S120": {"name": "Simran", "marks": 87},
    "S121": {"name": "Gaurav", "marks": 69},
    "S122": {"name": "Anjali", "marks": 92},
    "S123": {"name": "Vijay", "marks": 52},
    "S124": {"name": "Megha", "marks": 79},
    "S125": {"name": "Sanjay", "marks": 38},
    "S126": {"name": "Alok", "marks": 84},
    "S127": {"name": "Swati", "marks": 71},
    "S128": {"name": "Aditya", "marks": 96},
    "S129": {"name": "Kiran", "marks": 64},
    "S130": {"name": "Ishaan", "marks": 47}
}

while True:

    print("\n====================================")
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("====================================")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Topper and Lowest Scorer")
    print("7. Class Average")
    print("8. Pass and Fail Count")
    print("9. Generate Grades")
    print("10. Students Above Average")
    print("11. Top 5 Performers")
    print("12. Scholarship Students")
    print("13. Exit")

    choice = input("Enter Choice : ")

    # =====================================
    # 1. DISPLAY ALL STUDENTS
    # =====================================
    # Check kar rahe hain ki user ne option 1 select kiya hai ya nahi
    if choice == "1":

    # Heading display karna
        print("\nALL STUDENT RECORDS")

    # Dictionary ke sabhi Student IDs ko ek-ek karke access karna
        for sid in students:

        # Current Student ID, Name aur Marks print karna
            print(
                sid,                        # Student ID
                students[sid]["name"],      # Student ka Name
                students[sid]["marks"]      # Student ke Marks
        )
    # =====================================
    # 2. SEARCH STUDENT
    # =====================================
    # Check kar rahe hain ki user ne option 2 (Search Student) select kiya hai
    elif choice == "2":

    # User se Student ID lena aur uppercase me convert karna
    # Taaki s101 ya S101 dono same treat hon
        sid = input("Enter Student ID : ").upper()

    # Check karna ki entered Student ID dictionary me maujood hai ya nahi
        if sid in students:

        # Student mil gaya
            print("\nStudent Found")

        # Student ka name display karna
            print("Name :", students[sid]["name"])

        # Student ke marks display karna
            print("Marks :", students[sid]["marks"])

        else:

        # Agar ID dictionary me nahi mili
            print("Student Not Found")

    # =====================================
    # 3. ADD STUDENT
    # =====================================
    elif choice == "3":

        sid = input("Enter New Student ID : ").upper()

        if sid in students:

            print("Student ID Already Exists")

        else:

            name = input("Enter Name : ")

            marks = int(input("Enter Marks : "))

            if marks >= 0 and marks <= 100:

                students[sid] = {
                    "name": name,
                    "marks": marks
                }

                print("Student Added Successfully")

            else:

                print("Marks Must Be Between 0 and 100")

    # =====================================
    # 4. UPDATE MARKS
    # =====================================
    elif choice == "4":

        sid = input("Enter Student ID : ").upper()

        if sid in students:

            new_marks = int(input("Enter New Marks : "))

            if new_marks >= 0 and new_marks <= 100:

                students[sid]["marks"] = new_marks

                print("Marks Updated Successfully")

            else:

                print("Invalid Marks")

        else:

            print("Student Not Found")

    # =====================================
    # 5. DELETE STUDENT
    # =====================================
    elif choice == "5":

        sid = input("Enter Student ID : ").upper()

        if sid in students:

            del students[sid]

            print("Student Deleted Successfully")

        else:

            print("Student Not Found")

    # =====================================
    # 6. TOPPER AND LOWEST SCORER
    # =====================================
    elif choice == "6":

        topper_id = ""
        topper_marks = -1

        lowest_id = ""
        lowest_marks = 101

        for sid in students:

            if students[sid]["marks"] > topper_marks:

                topper_marks = students[sid]["marks"]
                topper_id = sid

            if students[sid]["marks"] < lowest_marks:

                lowest_marks = students[sid]["marks"]
                lowest_id = sid

        print("\nTOPPER")
        print(
            topper_id,
            students[topper_id]["name"],
            students[topper_id]["marks"]
        )

        print("\nLOWEST SCORER")
        print(
            lowest_id,
            students[lowest_id]["name"],
            students[lowest_id]["marks"]
        )

    # =====================================
    # 7. CLASS AVERAGE
    # =====================================
    elif choice == "7":

        total = 0

        for sid in students:

            total = total + students[sid]["marks"]

        average = total / len(students)

        print("Class Average =", round(average, 2))

    # =====================================
    # 8. PASS FAIL COUNT
    # =====================================
    elif choice == "8":

        pass_count = 0
        fail_count = 0

        for sid in students:

            if students[sid]["marks"] >= 50:

                pass_count = pass_count + 1

            else:

                fail_count = fail_count + 1

        print("Pass Students =", pass_count)
        print("Fail Students =", fail_count)

    # =====================================
    # 9. GENERATE GRADES
    # =====================================
    elif choice == "9":

        print("\nGRADE REPORT")

        for sid in students:

            marks = students[sid]["marks"]

            if marks >= 90:
                grade = "A"

            elif marks >= 75:
                grade = "B"

            elif marks >= 50:
                grade = "C"

            else:
                grade = "F"

            print(
                sid,
                students[sid]["name"],
                marks,
                grade
            )

    # =====================================
    # 10. ABOVE AVERAGE STUDENTS
    # =====================================
    elif choice == "10":

        total = 0

        for sid in students:

            total = total + students[sid]["marks"]

        average = total / len(students)

        print("\nAverage =", round(average, 2))
        print("Students Above Average")

        for sid in students:

            if students[sid]["marks"] > average:

                print(
                    sid,
                    students[sid]["name"],
                    students[sid]["marks"]
                )

    # =====================================
    # 11. TOP 5 PERFORMERS
    # =====================================
    elif choice == "11":

        temp_students = students.copy()

        print("\nTOP 5 PERFORMERS")

        count = 1

        while count <= 5:

            topper_id = ""
            highest_marks = -1

            for sid in temp_students:

                if temp_students[sid]["marks"] > highest_marks:

                    highest_marks = temp_students[sid]["marks"]
                    topper_id = sid

            print(
                count,
                topper_id,
                temp_students[topper_id]["name"],
                temp_students[topper_id]["marks"]
            )

            del temp_students[topper_id]

            count = count + 1

    # =====================================
    # 12. SCHOLARSHIP STUDENTS
    # =====================================
    elif choice == "12":

        scholarship_students = {}

        for sid in students:

            if students[sid]["marks"] > 85:

                scholarship_students[sid] = students[sid]

        print("\nSCHOLARSHIP STUDENTS")

        for sid in scholarship_students:

            print(
                sid,
                scholarship_students[sid]["name"],
                scholarship_students[sid]["marks"]
            )

    # =====================================
    # 13. EXIT
    # =====================================
    elif choice == "13":

        print("Thank You")
        break

    else:

        print("Invalid Choice")