"""4. Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament: 
runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
} 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs.  
Sample Output 
Players Scoring More Than 500 Runs: 
Virat 
Rohit 
Gill 
Pant 
 
Orange Cap Winner: Gill (698) 
 
Lowest Scorer: Hardik (278) 
 
Total Tournament Runs: 4657 
 
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja'] 
 
Players Between 400 and 600 Runs: 5"""

runs = { 
    "Virat": 645, 
    "Rohit": 512, 
    "Gill": 698, 
    "Rahul": 435, 
    "Hardik": 278, 
    "Pant": 534, 
    "Surya": 389, 
    "Jadeja": 301, 
    "Iyer": 455, 
    "KL": 410 
}

#=====================================
# 1. Display players scoring more than 500 runs.
#=====================================

for player, score in runs.items():
    if score > 500:
        print(player)
#=====================================
# 2. Find the Orange Cap winner.
#=====================================
orange_cap = None
orange_cap_score = 0
for player, score in runs.items():
    if score > orange_cap_score:
        orange_cap = player
        orange_cap_score = score
print("Orange Cap Winner: ",orange_cap,"(",orange_cap_score,")")
#=====================================
# 3. Find the lowest scorer.
#=====================================
lowest_scorer = None
lowest_score = float('inf')
for player, score in runs.items():
    if score < lowest_score:
        lowest_scorer = player
        lowest_score = score
print("Lowest Scorer: ",lowest_scorer,"(",lowest_score,")")
#=====================================
# 4. Calculate total runs scored.
#=====================================

total_runs = 0
for score in runs.values():
    total_runs += score
print("Total Tournament Runs: ",total_runs)
#=====================================
# 5. Create a list of players scoring below 400.
#=====================================
below_400 = []
for player, score in runs.items():
    if score < 400:
        below_400.append(player)
print("Players Scoring Below 400: ")
print(below_400)
#=====================================
# 6. Count players scoring between 400 and 600 runs.
#================================
count = 0
for score in runs.values():
    if 400 <= score <= 600:
        count += 1
print("Players Between 400 and 600 Runs: ",count)
#=====================================

"""output =
Virat
Rohit
Gill
Pant
Orange Cap Winner:  Gill ( 698 )
Lowest Scorer:  Hardik ( 278 )
Total Tournament Runs:  4657
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja']
Players Between 400 and 600 Runs:  5"""