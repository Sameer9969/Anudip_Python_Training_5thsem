"""Problem 10: Smart City Waste Collection Management System 
Problem Statement 
The amount of waste collected (in kilograms) from different sectors of a city is stored below. 
Sample Data 
    "Sector2": 180, 
    "Sector3": 510,  
    "Sector4": 275, ]
    "Sector5": 150, 
    "Sector6": 430, 
    "Sector7": 220, 
    "Sector8": 390, 
    "Sector9": 145, 
    "Sector10": 600 
} 
Tasks 
1. Display sectors generating more than 400 kg of waste.  
2. Find the sector generating maximum waste.  
3. Find the sector generating minimum waste.  
4. Calculate the total waste collected.  
5. Categorize sectors:  
o Low Waste (<200 kg)  
o Medium Waste (200–400 kg)  
o High Waste (>400 kg)  
6. Count sectors requiring awareness campaigns (waste generation >300 kg).  
7. Save the awareness campaign list to campaign_sectors.txt.  
Sample Output 
Sectors Generating More Than 400 kg Waste: 
Sector3 
Sector6 
Sector10 
 
Maximum Waste Generation: 
Sector10 (600 kg) 
 
Minimum Waste Generation: 
Sector9 (145 kg) 
 
Total Waste Collected: 3220 kg 
 
Low Waste: 
['Sector2', 'Sector5', 'Sector9'] 
 
Medium Waste: 
['Sector1', 'Sector4', 'Sector7', 'Sector8'] 
 
High Waste: 
['Sector3', 'Sector6', 'Sector10'] 
 
Sectors Requiring Awareness Campaign: 
Sector1 
Sector3 
Sector6 
Sector8 
Sector10 
 
Campaign Report Generated Successfully."""



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
    if students < 35:
        promotion_count += 1

print("\nCourses Requiring Promotion:", promotion_count)