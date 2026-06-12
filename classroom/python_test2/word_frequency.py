"""blem 19: Word Frequency Analyzer 
Problem Statement 
A text file contains the following paragraph. 
Sample Input/Data (article.txt) 
Python is easy to learn. 
Python is powerful. 
Python supports multiple programming paradigms. 
Programming with Python is enjoyable. 
Tasks 
1. Count the total number of words.  
2. Count the frequency of each word.  
3. Find the most frequently occurring word.  
4. Display words appearing only once.  
5. Display all unique words.  
Sample Output 
Total Words: 16 
 
Most Frequent Word: 
Python (4 times) 
 
Words Appearing Once: 
easy 
to 
learn 
powerful 
supports 
multiple 
paradigms 
with 
enjoyable 
 
Unique Words Count: 12"""


#=========================================
# Read file
file = open("article.txt", "r")

text = file.read()
file.close()

# Convert text into words
text = text.replace(".", "")
words = text.split()

# 1. Total number of words
total_words = len(words)
print("Total Words:", total_words)

# 2. Count frequency of each word
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
for word in frequency:
    print(word, ":", frequency[word])

# 3. Most frequent word
max_word = ""
max_count = 0

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        max_word = word

print("\nMost Frequent Word:")
print(max_word, "(", max_count, "times )")

# 4. Words appearing only once
print("\nWords Appearing Once:")
for word in frequency:
    if frequency[word] == 1:
        print(word)

# 5. Unique words count
print("\nUnique Words Count:", len(frequency))