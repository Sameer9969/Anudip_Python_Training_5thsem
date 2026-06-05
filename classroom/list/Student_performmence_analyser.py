# . Student Performance Analyzer 
# Problem Statement 
# A teacher has marks of students stored in a list. 
# marks = [78, 45, 92, 35, 88, 40, 99, 56] 
# Write a program to: 
# 1. Display all passed students (marks ≥ 40).  
# 2. Count the number of failed students.  
# 3. Find the highest and lowest marks without using max() or min().  
# 4. Create a new list containing marks above 75.

marks = [78, 45, 92, 35, 88, 40, 99, 56]
# 1. Display all passed students (marks ≥ 40).
passed_students = []
for mark in marks:
    if mark >= 40:
        passed_students.append(mark)
print("Passed Students:", passed_students)

# 2. Count the number of failed student
failed_count = 0

for mark in marks:
    if mark <= 40:
        failed_count += 1

print("Failed students =", failed_count)

# 3. Find the highest and lowest marks without using max() or min(). 
highest_mark = marks[0]
lowest_mark = marks[0]
for mark in marks:
    if mark > highest_mark:
        highest_mark = mark
    if mark < lowest_mark:
        lowest_mark = mark

print("Highest Mark =", highest_mark)
print("Lowest Mark =", lowest_mark)

# 4. Create a new list containing marks above 75.
above_75 = []
for mark in marks:
    if mark > 75:
        above_75.append(mark)

print("Marks above 75:", above_75)