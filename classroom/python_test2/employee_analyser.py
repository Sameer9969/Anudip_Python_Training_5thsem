"""Problem 20: Employee Performance Evaluation System 
Problem Statement 
Employee performance scores are stored below. 
Sample Data 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Categorize employees:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60)  
Sample Output 
Employees Scoring Above 80: 
EMP101 
EMP104 
EMP105 
EMP107 
 
Employees Needing Improvement: 3 
 
Top Performer: 
EMP105 (97) 
 
Average Score: 71.3 
 
Excellent: 
['EMP101', 'EMP105'] 
 
Good: 
['EMP102', 'EMP104', 'EMP107'] 
 
Average: 
['EMP108', 'EMP110'] 
 
Poor: 
['EMP103', 'EMP106', 'EMP109']"""



#======================================
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Employees Scoring Above 80
print("Employees Scoring Above 80:")
for emp in performance:
    if performance[emp] > 80:
        print(emp)

# 2. Count Employees Needing Improvement
improvement = 0
for emp in performance:
    if performance[emp] < 60:
        improvement = improvement + 1

print("\nEmployees Needing Improvement:", improvement)

# 3. Find Top Performer
top_emp = ""
top_score = 0

for emp in performance:
    if performance[emp] > top_score:
        top_score = performance[emp]
        top_emp = emp

print("\nTop Performer:")
print(top_emp, "(", top_score, ")")

# 4. Calculate Average Score
total = 0

for emp in performance:
    total = total + performance[emp]

average = total / len(performance)

print("\nAverage Score:", round(average, 1))

# 5. Categorize Employees
excellent = []
good = []
average_list = []
poor = []

for emp in performance:
    score = performance[emp]

    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average_list.append(emp)
    else:
        poor.append(emp)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average_list)

print("\nPoor:")
print(poor)