"""Assignment 6: Student Resume Analyzer 
Problem Statement 
A student enters a resume as plain text (Name, Skills, Education, Projects, Achievements). 
The system should: 
1. Count total words.  
2. Count total characters.  
3. Extract email IDs.  
4. Extract phone numbers.  
5. Count skills mentioned.  
6. Find repeated keywords.  
7. Identify the most frequently used word.  
8. Generate a skill frequency report.  
9. Detect duplicate skills.  
10. Create a summary dashboard.  
Expected Output 
Resume Analysis Report 
Total Words: 420 1222
Total Characters: 2650 
Email Found: 1 
Phone Numbers Found: 1 
Most Frequent Skill: Python 

Top 5 Keywords: 
Python 
SQL 
React 
Java 
Communication"""
# ==========================================
# Student Resume Analyzer
# Beginner Friendly Program
# ==========================================

# Resume stored as plain text

resume = """
Name: Sameer Singh

Email: sameer123@gmail.com

Phone: 9876543210

Education:
Bachelor of Computer Applications

Skills:
Python SQL Java React Python SQL Communication
Problem Solving Python Java React

Projects:
Library Management System using Python and SQL
Student Attendance System using Python
E-Commerce Website using React and Java

Achievements:
Won Coding Competition
Completed Python Certification
Best Project Award

Python SQL React Java Communication Python SQL
"""

# ==========================================
# Count Total Characters
# ==========================================

total_characters = len(resume)

# ==========================================
# Convert text into words
# ==========================================

words = resume.split()

# Count total words
total_words = len(words)

# ==========================================
# Extract Email IDs
# ==========================================

emails = []

for word in words:

    # Email me @ aur . hona chahiye
    if "@" in word and "." in word:

        emails.append(word)

# ==========================================
# Extract Phone Numbers
# ==========================================

phone_numbers = []

for word in words:

    # 10 digit mobile number check
    if word.isdigit() and len(word) == 10:

        phone_numbers.append(word)

# ==========================================
# Skills List
# Known skills stored manually
# ==========================================

skills_list = [
    "Python",
    "SQL",
    "Java",
    "React",
    "Communication",
    "Problem",
    "Solving"
]

# ==========================================
# Count Skills Mentioned
# ==========================================

skill_count = 0

for word in words:

    if word in skills_list:

        skill_count += 1

# ==========================================
# Skill Frequency Report
# ==========================================

skill_frequency = {}

for word in words:

    if word in skills_list:

        if word in skill_frequency:
            skill_frequency[word] += 1

        else:
            skill_frequency[word] = 1

# ==========================================
# Detect Duplicate Skills
# ==========================================

duplicate_skills = []

for skill in skill_frequency:

    if skill_frequency[skill] > 1:

        duplicate_skills.append(skill)

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
# Find Repeated Keywords
# ==========================================

repeated_keywords = []

for word in word_frequency:

    if word_frequency[word] > 1:

        repeated_keywords.append(word)

# ==========================================
# Find Most Frequently Used Word
# ==========================================

most_frequent_word = ""
highest_count = 0

for word in word_frequency:

    if word_frequency[word] > highest_count:

        highest_count = word_frequency[word]
        most_frequent_word = word

# ==========================================
# Find Most Frequent Skill
# ==========================================

most_frequent_skill = ""
max_skill_count = 0

for skill in skill_frequency:

    if skill_frequency[skill] > max_skill_count:

        max_skill_count = skill_frequency[skill]
        most_frequent_skill = skill

# ==========================================
# Top 5 Keywords
# ==========================================

top_keywords = []

for word in word_frequency:

    if len(top_keywords) < 5:

        top_keywords.append(word)

# ==========================================
# Display Results
# ==========================================

print("\n================================")
print("RESUME ANALYSIS REPORT")
print("================================")

print("Total Words      :", total_words)
print("Total Characters :", total_characters)

print("\nEmails Found")
print(emails)

print("\nPhone Numbers Found")
print(phone_numbers)

print("\nSkills Mentioned :", skill_count)

print("\nMost Frequent Word :", most_frequent_word)

print("Frequency          :", highest_count)

print("\nMost Frequent Skill :", most_frequent_skill)

# ==========================================
# Skill Frequency Report
# ==========================================

print("\n================================")
print("SKILL FREQUENCY REPORT")
print("================================")

for skill in skill_frequency:

    print(skill, "->", skill_frequency[skill])

# ==========================================
# Duplicate Skills
# ==========================================

print("\n================================")
print("DUPLICATE SKILLS")
print("================================")

print(duplicate_skills)

# ==========================================
# Repeated Keywords
# ==========================================

print("\n================================")
print("REPEATED KEYWORDS")
print("================================")

print(repeated_keywords)

# ==========================================
# Top 5 Keywords
# ==========================================

print("\n================================")
print("TOP 5 KEYWORDS")
print("================================")

for word in top_keywords:

    print(word)

# ==========================================
# Summary Dashboard
# ==========================================

print("\n================================")
print("SUMMARY DASHBOARD")
print("================================")

print("Total Words          :", total_words)

print("Total Characters     :", total_characters)

print("Email Found          :", len(emails))

print("Phone Numbers Found  :", len(phone_numbers))

print("Most Frequent Skill  :", most_frequent_skill)

print("Total Skills Found   :", skill_count)