"""3. Chat Message Analytics 
Problem Statement 
A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.  
Sample Output 
Message: 
Python is awesome and Python is easy to learn 
 
Total Characters: 45 
Total Words: 8 
 
Longest Word: awesome 
Shortest Word: is 
 
Occurrences of Python: 2 
 
Words Longer Than 4 Characters: 
['Python', 'awesome', 'Python', 'learn'] 
 
Vowels: 16 
Consonants: 22"""
#_____________________________________________
# 1.Count total characters. 
#_____________________________________________
message = "Python is awesome and Python is easy to learn"
total_characters = len(message)
print("Total Characters:", total_characters)
#_____________________________________________
# 2.Count total words. 
#_____________________________________________
count = 0
for char in message:
    if char == " ":
        count += 1
total_words = count + 1
print("Total Words:", total_words)
#_____________________________________________
# 3.Find the longest word. 
# 4.Find the shortest word.
#_____________________________________________
longest_word = ""
#split() bhi string ko character by character traverse karta hai,
#  space milne par current word ko list me add karta hai aur naya
#  word banana start karta hai.
words = message.split()

longest_word = words[0]
shortest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

    if len(word) < len(shortest_word):
        shortest_word = word

print("Longest Word :", longest_word)
print("Shortest Word:", shortest_word)
#_____________________________________________
# 5.Count how many times the word "Python" appears. 
#_____________________________________________  
count  = 0
for word in message.split():
    if word == "Python":
        count += 1
print("Occurrences of Python:", count)
#_____________________________________________
# 6.Create a list of words having more than 4 characters. 
#_____________________________________________
words = []
for word in message.split():
    if len(word) > 4:
        words.append(word)
print("Words Longer Than 4 Characters:", words)
#_____________________________________________
# 7.Display all words starting with a vowel. 
#_____________________________________________
vowels = "aeiouAEIOU"
for word in message.split():
    if word[0] in vowels:
        print(word)
#_____________________________________________
# 8.Count the number of vowels and consonants. 
#_____________________________________________
vowels = "aeiouAEIOU"
vowels_count = 0
consonants_count = 0
for char in message:
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        consonants_count += 1
print("Vowels:", vowels_count)
print("Consonants:", consonants_count)
#_____________________________________________
    
