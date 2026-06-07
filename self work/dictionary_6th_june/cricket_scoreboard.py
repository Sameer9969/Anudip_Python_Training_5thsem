"""4. Cricket Scoreboard Analysis 
Sample Data 
scores = { 
    "Virat": 78, 
    "Rohit": 112, 
    "Gill": 45, 
    "Rahul": 89, 
    "Hardik": 32, 
    "Jadeja": 61, 
    "Surya": 105, 
    "Pant": 95, 
    "Bumrah": 18, 
    "Shami": 25 
} 
Tasks 
• Display players who scored 50 or more runs.  
• Count the number of centuries.  
• Find the player with the highest score.  
• Create a list of players scoring below 30 runs.  
• Determine how many players scored between 50 and 99. """


# Cricket scoreboard dictionary
# Key = Player Name
# Value = Runs Scored

scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# ==================================================
# 1. Display players who scored 50 or more runs
# ==================================================

print("Players who scored 50 or more runs:")

# Loop through each player and score
for player, runs in scores.items():

    # Check if runs are 50 or more
    if runs >= 50:

        # Print player name
        print(player)

# ==================================================
# 2. Count the number of centuries
# ==================================================

# Variable to store century count
century_count = 0

# Loop through all scores
for runs in scores.values():

    # Check if runs are 100 or more
    if runs >= 100:

        # Increase century count by 1
        century_count += 1

# Display total centuries
print("Number of Centuries:", century_count)

# ==================================================
# 3. Find the player with the highest score
# ==================================================

# Variable to store highest scorer name
highest_player = ""

# Variable to store highest score
highest_score = 0

# Loop through each player and score
for player, runs in scores.items():

    # Check if current score is greater than highest score
    if runs > highest_score:

        # Update highest score
        highest_score = runs

        # Store player name
        highest_player = player

# Display highest scorer
print("Highest Scorer:", highest_player)

# Display highest score
print("Runs:", highest_score)

# ==================================================
# 4. Create a list of players scoring below 30 runs
# ==================================================

# Empty list to store player names
below_30 = []

# Loop through each player and score
for player, runs in scores.items():

    # Check if score is below 30
    if runs < 30:

        # Add player name to list
        below_30.append(player)

# Display list
print("Players scoring below 30 runs:", below_30)

# ==================================================
# 5. Determine how many players scored between 50 and 99
# ==================================================

# Variable to count players
count_50_to_99 = 0

# Loop through all scores
for runs in scores.values():

    # Check if score is between 50 and 99
    if runs >= 50 and runs <= 99:

        # Increase count by 1
        count_50_to_99 += 1

# Display count
print("Players scoring between 50 and 99:", count_50_to_99)