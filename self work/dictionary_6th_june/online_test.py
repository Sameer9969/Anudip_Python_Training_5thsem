"""quiz_scores = { 
    "S001": 18, 
    "S002": 12, 
    "S003": 9, 
    "S004": 20, 
    "S005": 14, 
    "S006": 7, 
    "S007": 16, 
    "S008": 10, 
    "S009": 19, 
    "S010": 13 
} 
(Quiz is out of 20 marks.) 
Tasks 
• Display students scoring 15 or above.  
• Count students scoring below 10.  
• Find the top performer.  
• Create a list of students who passed (≥ 10 marks).  
• Calculate the class average. """

# Quiz scores dictionary
# Key = Student ID
# Value = Quiz Marks (out of 20)

quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# ==================================================
# 1. Display students scoring 15 or above
# ==================================================

print("Students scoring 15 or above:")

# Loop through each student and score
for student, score in quiz_scores.items():

    # Check if score is 15 or more
    if score >= 15:

        # Print student ID
        print(student)

# ==================================================
# 2. Count students scoring below 10
# ==================================================

# Variable to store count
count = 0

# Loop through all scores
for score in quiz_scores.values():

    # Check if score is below 10
    if score < 10:

        # Increase count by 1
        count += 1

# Display count
print("Students scoring below 10:", count)

# ==================================================
# 3. Find the top performer
# ==================================================

# Variable to store student ID
top_student = ""

# Variable to store highest score
highest_score = 0

# Loop through each student and score
for student, score in quiz_scores.items():

    # Check if current score is greater than highest score
    if score > highest_score:

        # Update highest score
        highest_score = score

        # Store student ID
        top_student = student

# Display top performer
print("Top Performer:", top_student)

# Display highest score
print("Marks:", highest_score)

# ==================================================
# 4. Create a list of students who passed
# ==================================================

# Empty list to store passed students
passed_students = []

# Loop through each student and score
for student, score in quiz_scores.items():

    # Check if score is 10 or more
    if score >= 10:

        # Add student ID to list
        passed_students.append(student)

# Display passed students
print("Passed Students:")
print(passed_students)

# ==================================================
# 5. Calculate the class average
# ==================================================

# Variable to store total marks
total_marks = 0

# Loop through all scores
for score in quiz_scores.values():

    # Add score to total marks
    total_marks += score

# Find total number of students
total_students = len(quiz_scores)

# Calculate average marks
average_marks = total_marks / total_students

# Display average
print("Class Average:", average_marks)