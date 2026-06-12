"""Problem 9: Social Media Trend Analyzer 
Problem Statement 
Trending hashtags collected during an event are stored in a file named hashtags.txt. 
#AI 
#Python 
#AI 
#MachineLearning 
#DataScience 
#Python 
#AI 
#Coding 
#DataScience 
#Python 
Tasks 
1. Count occurrences of each hashtag.  
2. Display the top trending hashtag.  
3. Create a set of unique hashtags.  
4. Identify hashtags used more than twice.  
5. Generate a trend report file.  
Sample Output 
Hashtag Frequency: 
#AI : 3 
#Python : 3 
#MachineLearning : 1 
#DataScience : 2 
#Coding : 1 
 
Top Trending Hashtags: 
#AI 
#Python 
 
Unique Hashtags: 
{'#AI', '#Python', '#MachineLearning', '#DataScience', '#Coding'} 
 
Hashtags Used More Than Twice: 
#AI 
#Python 
 
Trend Report Generated Successfully."""

# Read hashtags from file

file = open("hashtag.txt", "r")

hashtags = []

for line in file:
    hashtags.append(line.strip())

file.close()

# Count frequency of each hashtag
frequency = {}

for tag in hashtags:
    if tag in frequency:
        frequency[tag] = frequency[tag] + 1
    else:
        frequency[tag] = 1

# Display frequency
print("Hashtag Frequency:")

for tag in frequency:
    print(tag, ":", frequency[tag])

# Find top trending hashtag(s)
highest = max(frequency.values())

print("\nTop Trending Hashtags:")

for tag in frequency:
    if frequency[tag] == highest:
        print(tag)

# Create set of unique hashtags
unique_hashtags = set(hashtags)

print("\nUnique Hashtags:")
print(unique_hashtags)

# Hashtags used more than twice
print("\nHashtags Used More Than Twice:")

for tag in frequency:
    if frequency[tag] > 2:
        print(tag)

# Generate trend report file
report = open("trend_report.txt", "w")

report.write("Hashtag Frequency:\n")

for tag in frequency:
    report.write(tag + " : " + str(frequency[tag]) + "\n")

report.close()

print("\nTrend Report Generated Successfully.")
###########################cd classroom\python_test3
############################ python cyber_security_login_audit.py