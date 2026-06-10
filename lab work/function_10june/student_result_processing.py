"""3. Student Result Processing System 
Problem Statement 
Student marks are stored in results.txt. 
File Format 
S101,Anuj,85 
S102,Rahul,72 
S103,Priya,96 
S104,Neha,68 
S105,Amit,39 
S106,Sneha,54 
S107,Karan,91 
S108,Pooja,78 
S109,Rohit,47 
S110,Anjali,88 
Requirements 
Write a program to: 
1. Display all student records.  
2. Search a student using Student ID.  
3. Find topper and lowest scorer.  
4. Calculate class average.  
5. Count pass and fail students.  
6. Generate grades:  
o A (90+)  
o B (75–89)  
o C (40–74)  
o F (<40)  
7. Write grade reports into a new file named grades.txt. """

# Student Result Processing System

# results.txt file ko read mode me open kar rahe hain
file = open('results.txt', 'r')

# Students ka data store karne ke liye empty list
students = []

# File ki har line ko read karenge
for line in file:
    
    # Line ke end me jo extra newline (\n) hota hai use remove kar rahe hain
    line = line.strip()
    
    # Comma ke basis par data ko alag kar rahe hain
    data = line.split(",")
    
    # Student ID store kar rahe hain
    sid = data[0]
    
    # Student Name store kar rahe hain
    name = data[1]
    
    # Marks ko integer me convert kar rahe hain
    marks = int(data[2])
    
    # Dictionary bana kar list me add kar rahe hain
    students.append({
        "id": sid,
        "name": name,
        "marks": marks
    })

# File close kar rahe hain
file.close()

# -------------------------------
# 1. Display All Student Records
# -------------------------------
print("ALL STUDENT RECORDS")
print("-" * 40)

for student in students:
    print(student["id"], student["name"], student["marks"])

# -------------------------------
# 2. Search Student By ID
# -------------------------------
print("\nSEARCH STUDENT")

# User se Student ID input le rahe hain
search_id = input("Enter Student ID: ")

found = False

for student in students:
    
    # Agar ID match ho jaye
    if student["id"] == search_id:
        print("Student Found")
        print("Name :", student["name"])
        print("Marks:", student["marks"])
        found = True
        break

# Agar koi student na mile
if found == False:
    print("Student Not Found")

# -------------------------------
# 3. Find Topper and Lowest Scorer
# -------------------------------

# Pehle student ko topper maan rahe hain
topper = students[0]

# Pehle student ko lowest scorer maan rahe hain
lowest = students[0]

for student in students:

    # Agar marks topper se zyada hain
    if student["marks"] > topper["marks"]:
        topper = student

    # Agar marks lowest se kam hain
    if student["marks"] < lowest["marks"]:
        lowest = student

print("\nTOPPER")
print(topper["name"], "-", topper["marks"])

print("\nLOWEST SCORER")
print(lowest["name"], "-", lowest["marks"])

# -------------------------------
# 4. Calculate Class Average
# -------------------------------

total = 0

# Sabhi marks ko add karenge
for student in students:
    total += student["marks"]

# Average nikal rahe hain
average = total / len(students)

print("\nCLASS AVERAGE =", average)

# -------------------------------
# 5. Count Pass and Fail Students
# -------------------------------

pass_count = 0
fail_count = 0

for student in students:

    # 40 ya usse zyada marks wale pass
    if student["marks"] >= 40:
        pass_count += 1
    else:
        fail_count += 1

print("\nPASS STUDENTS =", pass_count)
print("FAIL STUDENTS =", fail_count)

# -------------------------------
# 6 & 7. Generate Grades
# Write into grades.txt
# -------------------------------

# grades.txt file write mode me open kar rahe hain
grade_file = open('grades.txt', 'w')

print("\nGRADE REPORT")

for student in students:

    marks = student["marks"]

    # Grade decide kar rahe hain
    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 40:
        grade = "C"

    else:
        grade = "F"

    # Output screen par print kar rahe hain
    print(student["id"], student["name"], marks, grade)

    # File me data write kar rahe hain
    grade_file.write(
        student["id"] + "," +
        student["name"] + "," +
        str(marks) + "," +
        grade + "\n"
    )

# File close kar rahe hain
grade_file.close()

print("\nGrades successfully saved in grades.txt")
# cd "lab work/function_10june"