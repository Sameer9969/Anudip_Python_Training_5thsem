"""7. Username Generator System 
Problem Statement 
A student enters: 
Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics.  
Sample Output 
Original Name: Rahul Sharma 
 
Generated Username: 
rahulsharma2026 
 
Username Length: 15 
 
Vowels: 5 
Consonants: 10 
 
Status: Username Generated Successfully"""

#----------------------------------------------
# Username Generator System
#----------------------------------------------

# Original name given by user
name = "Rahul Sharma"

# Display original name
print("Original Name:", name)

#----------------------------------------------
# 1. Remove spaces
#----------------------------------------------

username = ""

# Traverse each character of the name
for ch in name:

    # Add only those characters which are not spaces
    if ch != " ":
        username += ch

#----------------------------------------------
# 2. Convert to lowercase
#----------------------------------------------

# Convert all letters to lowercase
username = username.lower()

#----------------------------------------------
# 3. Append current year (2026)
#----------------------------------------------

# Add year at the end of username
username = username + "2026"

# Display generated username
print("\nGenerated Username:", username)

#----------------------------------------------
# 4. If username length exceeds 12,
#    keep only first 12 characters
#----------------------------------------------

# Check length of username
if len(username) > 12:

    # Keep only first 12 characters
    username = username[:12]

#----------------------------------------------
# Display username length
#----------------------------------------------

print("\nUsername Length:", len(username))

#----------------------------------------------
# 5. Count vowels
#----------------------------------------------

vowel_count = 0

# Vowels string for checking
vowels = "aeiou"

# Traverse username character by character
for ch in username:

    # Check whether character is a vowel
    if ch in vowels:
        vowel_count += 1

#----------------------------------------------
# 6. Count consonants
#----------------------------------------------

consonant_count = 0

# Traverse username character by character
for ch in username:

    # Check if character is alphabet
    if ch.isalpha():

        # Check if it is not a vowel
        if ch not in vowels:
            consonant_count += 1

#----------------------------------------------
# 7. Display statistics
#----------------------------------------------

print("\nVowels:", vowel_count)
print("Consonants:", consonant_count)

print("\nStatus: Username Generated Successfully")