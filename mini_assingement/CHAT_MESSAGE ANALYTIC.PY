"""Assignment 3: Chat Message Analytics Dashboard 
Problem Statement 
A messaging application wants to analyze chat messages. 
Store at least 20 chat messages in a list. 
Requirements 
For each message: 
1. Count total words.  
2. Count total characters.  
3. Count vowels and consonants.  
4. Find longest word.  
5. Find shortest word.  
6. Count occurrence of each word.  
7. Display repeated words.  
8. Display words starting with vowels.  
9. Display words longer than 5 characters.  
10. Create a dictionary containing word frequencies.  
Challenge 
Generate a report showing: 
Most Frequently Used Word 
Longest Message 
Shortest Message 
Average Words Per Message """

# ==========================================
# Chat Message Analytics Dashboard
# Beginner Friendly Program
# ==========================================

# Store at least 20 chat messages in a list

messages = [
    "hello how are you",
    "i am fine thank you",
    "python is easy to learn",
    "today is a beautiful day",
    "welcome to the programming class",
    "practice makes a person perfect",
    "coding improves problem solving",
    "have a nice day",
    "please complete your assignment",
    "learning python is fun",
    "chat applications are useful",
    "data analysis is interesting",
    "i like reading books",
    "this is a sample message",
    "keep working hard",
    "success comes with dedication",
    "education is important",
    "always believe in yourself",
    "communication builds relationships",
    "thank you everyone"
]

# ==========================================
# Variables for Challenge Report
# ==========================================

total_words_all_messages = 0

longest_message = messages[0]
shortest_message = messages[0]

# Dictionary to store frequency of all words
word_frequency = {}

# ==========================================
# Analyze Each Message
# ==========================================

for message in messages:

    print("\n================================")
    print("Message :", message)
    print("================================")

    # --------------------------------------
    # Split message into words
    # --------------------------------------
    words = message.split()

    # Count total words
    total_words = len(words)

    # Add into overall total
    total_words_all_messages += total_words

    # --------------------------------------
    # Count total characters
    # --------------------------------------
    total_characters = len(message)

    # --------------------------------------
    # Count vowels and consonants
    # --------------------------------------
    vowels = 0
    consonants = 0

    for ch in message:

        if ch.isalpha():

            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    # --------------------------------------
    # Find longest word
    # --------------------------------------
    longest_word = words[0]

    for word in words:

        if len(word) > len(longest_word):
            longest_word = word

    # --------------------------------------
    # Find shortest word
    # --------------------------------------
    shortest_word = words[0]

    for word in words:

        if len(word) < len(shortest_word):
            shortest_word = word

    # --------------------------------------
    # Count occurrence of each word
    # --------------------------------------
    local_frequency = {}

    for word in words:

        if word in local_frequency:
            local_frequency[word] += 1
        else:
            local_frequency[word] = 1

    # --------------------------------------
    # Display repeated words
    # --------------------------------------
    repeated_words = []

    for word in local_frequency:

        if local_frequency[word] > 1:
            repeated_words.append(word)

    # --------------------------------------
    # Words starting with vowels
    # --------------------------------------
    vowel_words = []

    for word in words:

        if word[0].lower() in "aeiou":
            vowel_words.append(word)

    # --------------------------------------
    # Words longer than 5 characters
    # --------------------------------------
    long_words = []

    for word in words:

        if len(word) > 5:
            long_words.append(word)

    # --------------------------------------
    # Create overall word frequency dictionary
    # --------------------------------------
    for word in words:

        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # --------------------------------------
    # Display Message Report
    # --------------------------------------

    print("Total Words        :", total_words)
    print("Total Characters   :", total_characters)
    print("Vowels             :", vowels)
    print("Consonants         :", consonants)

    print("Longest Word       :", longest_word)
    print("Shortest Word      :", shortest_word)

    print("Word Frequency     :", local_frequency)

    print("Repeated Words     :", repeated_words)

    print("Words Starting Vowel :", vowel_words)

    print("Words > 5 Characters :", long_words)

    # --------------------------------------
    # Find longest message
    # --------------------------------------
    if len(message) > len(longest_message):
        longest_message = message

    # --------------------------------------
    # Find shortest message
    # --------------------------------------
    if len(message) < len(shortest_message):
        shortest_message = message

# ==========================================
# Most Frequently Used Word
# ==========================================

most_used_word = ""
highest_count = 0

for word in word_frequency:

    if word_frequency[word] > highest_count:

        highest_count = word_frequency[word]
        most_used_word = word

# ==========================================
# Average Words Per Message
# ==========================================

average_words = total_words_all_messages / len(messages)

# ==========================================
# Final Challenge Report
# ==========================================

print("\n\n================================")
print("CHAT ANALYTICS REPORT")
print("================================")

print("Most Frequently Used Word :", most_used_word)

print("Frequency                 :", highest_count)

print("\nLongest Message :")
print(longest_message)

print("\nShortest Message :")
print(shortest_message)

print("\nAverage Words Per Message :", average_words)

print("\n================================")
print("WORD FREQUENCY DICTIONARY")
print("================================")

print(word_frequency)