"""Problem Statement 
A batsman's scores in different matches are stored in a list. 
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
Write a program to: 
• Count half-centuries and centuries.  
• Find the highest score.  
• Display all scores below 20.  
• Calculate the average score. """

scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Count half-centuries and centuries
half_centuries = 0
centuries = 0

for score in scores:
    if score >= 50 and score < 100:
        half_centuries += 1
    elif score >= 100:
        centuries += 1

print("Half-Centuries:", half_centuries)
print("Centuries:", centuries)

# Find the highest score.
highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print("Highest Score:", highest_score)

# Display all scores below 20.
print("Scores below 20:")
for score in scores:
    if score < 20:
        print(score)

# Calculate the average score.  
avg_score = 0
for score in scores:
    avg_score += score
avg_score = avg_score /len(scores)

print("Average Score:", avg_score)


