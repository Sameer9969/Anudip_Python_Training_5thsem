player = []

for i in range(1, 11):
    score = int(input("Enter score of player: "))
    player.append(score)

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