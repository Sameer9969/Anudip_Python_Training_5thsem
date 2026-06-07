"""1. Student Marks Analysis 
Sample Data 
marks = { 
    "Aarav": 78, 
    "Diya": 92, 
    "Rohan": 45, 
    "Ishita": 88, 
    "Kabir": 56, 
    "Meera": 39, 
    "Arjun": 95, 
    "Saanvi": 67, 
    "Vivaan": 82, 
    "Anaya": 51 
} 
Tasks 
• Display students scoring 80 or above.  
• Count the number of students who failed (marks < 40).  
• Find the highest scorer.  
• Create a list of students scoring between 60 and 75.  
• Assign grades:  
o A: ≥ 90  
o B: 75–89  
o C: 50–74  
o F: < 50 """

marks = { 
    "Aarav": 78, 
    "Diya": 92, 
    "Rohan": 45, 
    "Ishita": 88, 
    "Kabir": 56, 
    "Meera": 39, 
    "Arjun": 95, 
    "Saanvi": 67, 
    "Vivaan": 82, 
    "Anaya": 51 
} 

# Display students scoring 80 or above.
print("Students scoring 80 or above:")
for student, score in marks.items():
    if score >= 80:
        print(student)

# Count the number of students who failed (marks < 40).
print("\nNumber of students who failed:")
failed_count = 0
for score in marks.values():
    if score < 40:
        failed_count += 1
print(failed_count)

# Find the highest scorer.
# Highest scorer ka naam store karne ke liye variable
highest_student = ""

# Highest marks store karne ke liye variable
# Starting me 0 rakha hai taaki koi bhi marks isse bade hon
highest_marks = 0

# Dictionary ke har key-value pair par loop chalega
# student me naam aur score me marks aayenge
for student, score in marks.items():

    # Check karo ki current student ke marks
    # ab tak ke highest marks se zyada hain ya nahi
    if score > highest_marks:

        # Agar zyada hain to highest marks update kar do
        highest_marks = score

        # Aur us student ka naam bhi store kar lo
        highest_student = student

# Loop khatam hone ke baad highest scorer ka naam print hoga
print("Highest Scorer:", highest_student)

# Highest scorer ke marks print honge
print("Marks:", highest_marks)

#Create a list of students scoring between 60 and 75.  
# • Assign grades:  
# o A: ≥ 90  
# o B: 75–89  
# o C: 50–74  
# o F: < 50 
print("\nStudents scoring between 60 and 75:")
for student, score in marks.items():
    if 60 <= score <= 75:
        print(student)

print("\nGrades:")
for student, score in marks.items():
    if score >= 90:
        print(student, ": A")
    elif 75 <= score <= 89:
        print(student, ": B")
    elif 50 <= score <= 74:
        print(student, ": C")
    else:
        print(student, ": F")
