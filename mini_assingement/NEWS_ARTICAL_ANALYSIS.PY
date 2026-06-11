"""Assignment 5: News Article Text Analyzer 
Problem Statement 
A news agency wants to analyze the content of an article. 
Use a paragraph containing at least 300 words. 
Requirements 
1. Count total characters.  
2. Count total words.  
3. Count total sentences.  
4. Count vowels and consonants.  
5. Find longest word.  
6. Find shortest word.  
7. Find the most frequent word.  
8. Create a dictionary of word f11requencies.  
9. Display words appearing only once.  
10. Display words appearing more than 5 times.  
11. Count words starting with each alphabet.  
12. Display all unique words.  
Challenge 
Generate a complete text summary: 
Total Words 
Total Sentences 
Average Word Length 
Most Frequent Word 
Vocabulary Size"""


# ==========================================
# News Article Text Analyzer
# Beginner Friendly Program
# ==========================================

# News article (300+ words)

article = """
India is one of the fastest growing economies in the world. The country
has made significant progress in technology, education, healthcare, and
infrastructure. In recent years, digital transformation has changed the
way people communicate, learn, and work. Many government initiatives
have encouraged innovation and entrepreneurship among young citizens.

The education sector has seen major improvements with the introduction
of online learning platforms. Students can now access quality education
from different parts of the country. Teachers are using technology to
make learning more interactive and engaging. As a result, students are
developing new skills that help them compete in a global environment.

Healthcare services have also improved due to advancements in medical
technology. Hospitals are adopting modern equipment to provide better
treatment to patients. Telemedicine services allow doctors to consult
patients remotely. This has become especially useful for people living
in rural areas where healthcare facilities may 
"""

# ==========================================
# Count Total Characters
# ==========================================

total_characters = len(article)

# ==========================================
# Count Total Sentences
# ==========================================

total_sentences = article.count(".")

# ==========================================
# Count Vowels and Consonants
# ==========================================

vowels = 0
consonants = 0

for ch in article:

    if ch.isalpha():

        if ch.lower() in "aeiou":
            vowels += 1

        else:
            consonants += 1

# ==========================================
# Convert text into words
# Remove punctuation
# ==========================================

clean_text = article.lower()

clean_text = clean_text.replace(".", "")
clean_text = clean_text.replace(",", "")
clean_text = clean_text.replace("\n", " ")

words = clean_text.split()

# ==========================================
# Count Total Words
# ==========================================

total_words = len(words)
2
# ==========================================
# Find Longest Word
# ==========================================

longest_word = words[0]

for word in words:

    if len(word) > len(longest_word):
        longest_word = word

# ==========================================
# Find Shortest Word
# ==========================================

shortest_word = words[0]

for word in words:

    if len(word) < len(shortest_word):
        shortest_word = word

# ==========================================
# Create Word Frequency Dictionary
# ==========================================

word_frequency = {}

for word in words:

    if word in word_frequency:
        word_frequency[word] += 1

    else:
        word_frequency[word] = 1

# ==========================================
# Find Most Frequent Word
# ==========================================

most_frequent_word = ""
highest_count = 0

for word in word_frequency:

    if word_frequency[word] > highest_count:

        highest_count = word_frequency[word]
        most_frequent_word = word

# ==========================================
# Display Words Appearing Only Once
# ==========================================

single_words = []

for word in word_frequency:

    if word_frequency[word] == 1:
        single_words.append(word)

# ==========================================
# Display Words Appearing More Than 5 Times
# ==========================================

more_than_five = []

for word in word_frequency:

    if word_frequency[word] > 5:
        more_than_five.append(word)

# ==========================================
# Count Words Starting With Each Alphabet
# ==========================================

alphabet_count = {}

for word in words:

    first_letter = word[0]

    if first_letter in alphabet_count:
        alphabet_count[first_letter] += 1

    else:
        alphabet_count[first_letter] = 1

# ==========================================
# Display Unique Words
# ==========================================

unique_words = list(word_frequency.keys())

# ==========================================
# Average Word Length
# ==========================================

total_word_length = 0

for word in words:
    total_word_length += len(word)

average_word_length = total_word_length / total_words

# ==========================================
# Vocabulary Size
# Unique words count
# ==========================================

vocabulary_size = len(unique_words)

# ==========================================
# Display Results
# ==========================================

print("\n================================")
print("NEWS ARTICLE ANALYSIS")
print("================================")

print("Total Characters :", total_characters)
print("Total Words      :", total_words)
print("Total Sentences  :", total_sentences)

print("Vowels           :", vowels)
print("Consonants       :", consonants)

print("Longest Word     :", longest_word)
print("Shortest Word    :", shortest_word)

print("Most Frequent Word :", most_frequent_word)
print("Frequency          :", highest_count)

print("\n================================")
print("WORD FREQUENCY DICTIONARY")
print("================================")
print(word_frequency)

print("\n================================")
print("WORDS APPEARING ONLY ONCE")
print("================================")
print(single_words)

print("\n================================")
print("WORDS APPEARING MORE THAN 5 TIMES")
print("================================")
print(more_than_five)

print("\n================================")
print("WORDS STARTING WITH EACH ALPHABET")
print("================================")
print(alphabet_count)

print("\n================================")
print("ALL UNIQUE WORDS")
print("================================")
print(unique_words)

# ==========================================
# Challenge Summary Report
# ==========================================

print("\n================================")
print("TEXT SUMMARY REPORT")
print("================================")

print("Total Words         :", total_words)
print("Total Sentences     :", total_sentences)
print("Average Word Length :", round(average_word_length, 2))
print("Most Frequent Word  :", most_frequent_word)
print("Vocabulary Size     :", vocabulary_size)