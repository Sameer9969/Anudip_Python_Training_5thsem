"""Problem 7: Cricket Tournament Statistics 
Problem Statement 
Runs scored by players in a tournament are given below. 
Sample Data 
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
1. Find the Orange Cap winner.  
2. Find the lowest scorer.  
3. Calculate total runs scored.  
4. Display players scoring more than 500 runs.  
5. Create a list of players scoring below 400.  
Sample Output 
Orange Cap Winner: 
Gill (698 runs) 
 
Lowest Scorer: 
Hardik (278 runs) 
 
Total Runs: 4657 
 
Players Scoring Above 500: 
Virat 
Rohit 
Gill 
Pant 
 
Players Scoring Below 400: 
['Hardik', 'Surya', 'Jadeja']"""


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

# 1. Orange Cap Winner
highest_player = ""
highest_runs = 0

for player in runs:
    if runs[player] > highest_runs:
        highest_runs = runs[player]
        highest_player = player

print("Orange Cap Winner:")
print(highest_player, "(", highest_runs, "runs )")

# 2. Lowest Scorer
lowest_player = list(runs.keys())[0]
lowest_runs = runs[lowest_player]

for player in runs:
    if runs[player] < lowest_runs:
        lowest_runs = runs[player]
        lowest_player = player

print("\nLowest Scorer:")
print(lowest_player, "(", lowest_runs, "runs )")

# 3. Total Runs
total_runs = 0

for player in runs:
    total_runs = total_runs + runs[player]

print("\nTotal Runs:", total_runs)

# 4. Players Scoring Above 500 Runs
print("\nPlayers Scoring Above 500:")

for player in runs:
    if runs[player] > 500:
        print(player)

# 5. Players Scoring Below 400 Runs
below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:")
print(below_400)