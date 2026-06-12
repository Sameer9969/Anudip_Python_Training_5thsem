"""Problem 2: Student Scholarship Evaluation System 
Problem Statement 
The marks obtained by students in the final examination are stored as follows: 
Sample Data 
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
Tasks 
1. Display students scoring above 85 marks.  
2. Find the topper.  
3. Find the student with the lowest marks.  
4. Calculate class average marks.  
5. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
6. Create a list of scholarship students (marks ≥ 90).  
Sample Output 
Students Scoring Above 85: 
Anuj 
Priya 
Sneha 
Anjali 
 
Topper: 
Sneha (95) 
 
Lowest Scorer: 
Rohit (47) 
 
Average Marks: 76.4 
 
Scholarship Students: 
['Anuj', 'Sneha', 'Anjali']"""


marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
#==========================================
# 1. Display students scoring above 85 marks.
#==========================================
print("Students Scoring Above 85:")
for student in marks:
    if marks[student] > 85 :
        print(student)
#==========================================
# 2. Find the topper.  
#==========================================
topper = None
highest_marks = -1

for student, score in marks.items():
    if score > highest_marks:
        highest_marks = score
        topper = student

print("\nTopper:")
print(topper, "(", highest_marks, ")")
#==========================================
# 3. Find the student with the lowest marks.
#==========================================
lowest = float('inf')
for student in marks:
    if marks[student] < lowest:
        lowest = marks[student]
        lowest_student = student
print("Lowest Scorer:")
print(lowest_student, "(", lowest, ")")

#==========================================
# 4. Calculate class average marks.
#==========================================
total = 0
for score in marks.values():
    total += score
average = total / len(marks)
print("Average Marks:", average)
#==========================================
# 5. Generate grades:  
#o A (90+)  
#o B (75–89)  
#o C (50–74)  
#o F (<50)  
#==========================================
for student in marks:
    score = marks[student]
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    print(student, "-", score, "-", grade)
#==========================================
# 6. Create a list of scholarship students (marks ≥ 90).
#==========================================
print("scholorship Students:")
for student in marks:
    score = marks[student]
    if score >= 90:
        print(student)
#==========================================

