# Problem Statement

# 10 players ke scores input lo aur unme se sabse zyada score karne wale player ko identify karo.

# Requirements
# User se 10 players ke scores input lo aur unhe ek list me store karo.
# Sabhi players ke scores display karo.
# Loop ka use karke maximum score find karo (built-in max() function ka use nahi karna hai).
# Maximum score kis player ne banaya hai, uska player number bhi display karo.
# Output me maximum score aur player number print karo.
#list formation
player = []
#taking value in list
for i in range(1, 11):
    scores = int(input("Enter score of player: "))
    player.append(scores)

print("Scores of players:", player)

max_score = player[0]
player_no = 1

for index in range(1, len(player)):
    if player[index] > max_score:
        max_score = player[index]
        player_no = index + 1

print("Maximum Score =", max_score)
print("Player Number =", player_no)
print("--------------------------------")