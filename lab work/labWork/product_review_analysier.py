"""5. Product Review Analyzer 
Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.  

Sample Output 
Total Words: 8 
 
Word Frequencies: 
This -> 1 
product -> 1 
is -> 1 
excellent -> 3 
and -> 1 
very -> 1 
useful -> 1 
 
Most Frequent Word: excellent 
 
Words Appearing Once: 
['This', 'product', 'is', 'and', 'very', 'useful'] 
 
Unique Words: 
['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']"""

#---------------------------------------
#----------------------------------------------
# Product Review Analyzer
#----------------------------------------------

review = "This product is excellent excellent excellent and very useful"

#----------------------------------------------
# Convert sentence into words
#----------------------------------------------

words = review.split()

print(words)

#----------------------------------------------
# 1. Count total words
#----------------------------------------------
print("Total Words:", len(words))

#----------------------------------------------
# 2. Create dictionary of word frequencies
#----------------------------------------------
frequency = {}

for word in words:
    if (word in frequency):
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")

for word in frequency:
    print(word, "->", frequency[word])

#----------------------------------------------
# 3. Find most frequent word
#----------------------------------------------
max_word = ""
max_count = 0

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        max_word = word

print("\nMost Frequent Word:", max_word)

#----------------------------------------------
# 4. Find words appearing only once
#----------------------------------------------
once_words = []

for word in frequency:
    if frequency[word] == 1:
        once_words.append(word)

print("\nWords Appearing Once:")
print(once_words)

#----------------------------------------------
# 5. Count words having more than 5 characters
#----------------------------------------------
count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("\nWords Having More Than 5 Characters:", count)

#----------------------------------------------
# 6. Display words in reverse order
#----------------------------------------------
print("\nWords in Reverse Order:")

for i in range(len(words)-1,-1,-1 ):
    print(words[i], end=" ")

#----------------------------------------------
# 7. Create list of unique words
#----------------------------------------------
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("\n\nUnique Words:")
print(unique_words)