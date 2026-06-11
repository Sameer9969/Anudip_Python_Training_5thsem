"""Problem 9: University Course Enrollment Management System 
Problem Statement 
Student enrollment data for university courses is stored below. 
Sample Data 
enrollment = { 
    "Python": 45, 
    "Java": 38, 
    "Data Science": 52, 
    "Web Development": 34, 
    "Machine Learning": 41, 
    "Cloud Computing": 29, 
    "Cyber Security": 33, 
    "DBMS": 48, 
    "Networking": 26, 
} 
"Operating Systems": 37 
Tasks 
1. Display courses having more than 40 enrollments.  
2. Find the most and least popular courses.  
3. Calculate total enrollments.  
4. Create lists:  
o High Demand (>40)  
o Medium Demand (30–40)  
o Low Demand (<30)  
5. Count courses requiring promotional activities (<35 enrollments).  
Sample Output 
Courses with More Than 40 Enrollments: 
Python 
Data Science 
Machine Learning 
DBMS 
Most Popular Course: 
Data Science (52 students) 
Least Popular Course: 
Networking (26 students) 
Total Enrollments: 383 
High Demand: 
['Python', 'Data Science', 'Machine Learning', 'DBMS'] 
Medium Demand: 
['Java', 'Web Development', 'Cyber Security', 'Operating Systems'] 
Low Demand: 
['Cloud Computing', 'Networking'] 
Courses Requiring Promotion: 3"""


# University Course Enrollment Management System

enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}

# 1. Display courses having more than 40 enrollments
print("Courses with More Than 40 Enrollments:")
for course in enrollment:
    if enrollment[course] > 40:
        print(course)

# 2. Find the most and least popular courses
most_course = max(enrollment, key=enrollment.get)
least_course = min(enrollment, key=enrollment.get)

print("\nMost Popular Course:")
print(most_course, f"({enrollment[most_course]} students)")

print("\nLeast Popular Course:")
print(least_course, f"({enrollment[least_course]} students)")

# 3. Calculate total enrollments
total = sum(enrollment.values())
print("\nTotal Enrollments:", total)

# 4. Create demand lists
high_demand = []
medium_demand = []
low_demand = []

for course in enrollment:
    students = enrollment[course]

    if students > 40:
        high_demand.append(course)
    elif 30 <= students <= 40:
        medium_demand.append(course)
    else:
        low_demand.append(course)

print("\nHigh Demand:")
print(high_demand)

print("\nMedium Demand:")
print(medium_demand)

print("\nLow Demand:")
print(low_demand)

# 5. Count courses requiring promotion (<35 enrollments)
promotion_count = 0

for students in enrollment.values():
    if students < 35:00
    promotion_count += 1

print("\nCourses Requiring Promotion:", promotion_count)