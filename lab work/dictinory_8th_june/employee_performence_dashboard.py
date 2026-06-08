"""2. Employee Performance Dashboard 
Problem Statement 
Employee performance scores are stored as: 
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
5. Create separate lists:  
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
 
Top Performer: EMP105 (97) 
 
Employees Needing Improvement: 3 
 
Average Score: 71.3 
 
Excellent: 
['EMP101', 'EMP105'] 
 
Good: 
['EMP102', 'EMP104', 'EMP107'] 
 
Average: 
['EMP108', 'EMP110'] 
 
Poor: 
['EMP103', 'EMP106', 'EMP109'] """


 
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
#===========================================
# 1. Display employees scoring above 80.  
#===========================================
print("employees that is scoring above 80:")
for emp,score in performance.items():
    if score > 80:
        print(emp)
#===========================================
# 2. Count employees needing improvement (score < 60).  
#===========================================
count = 0
for emp,score in performance.items():
    if score < 60:
        count += 1
print("Employees Needing Improvement: ",count)
#===========================================
# 3. Find the top performer.  
#===========================================
top_performer = None
top_score = 0
for emp,score in performance.items():
    if score > top_score:
        top_performer = emp
        top_score = score
print("Top Performer: ",top_performer,"(",top_score,")")
#===========================================
# 4. Calculate average performance score.  
#===========================================
total_score = 0
for score in performance.values():
    total_score += score
average_score = total_score / len(performance)
print("Average Score: ",average_score)
#===========================================
# 5.Create separate lists:  
#o Excellent (≥ 90)  
#o Good (75–89)  
#o Average (60–74)  
#o Poor (< 60)
#===========================================
excellent = []
good = []
average = []
poor = []
for emp,score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif 75 <= score <= 89:
        good.append(emp)
    elif 60 <= score <= 74:
        average.append(emp)
    else:
        poor.append(emp)
print("Excellent: ")
print(excellent)
print("Good: ")
print(good)
print("Average: ")
print(average)
print("Poor: ")
print(poor)
#===========================================

"""output =
employees that is scoring above 80:
EMP101
EMP104
EMP105
EMP107
Employees Needing Improvement:  3
Top Performer:  EMP105 ( 97 )
Average Score:  71.3
Excellent: 
['EMP101', 'EMP105']
Good: 
['EMP102', 'EMP104', 'EMP107']
Average: 
['EMP108', 'EMP110']
Poor: 
['EMP103', 'EMP106', 'EMP109']"""