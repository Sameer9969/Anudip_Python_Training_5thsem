"""9. License Key Verification System 
Problem Statement 
A software license key is entered: 
ABCD-EFGH-IJKL-MNOP 
Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.  
7. Display whether the key format is valid.  
Sample Output 
License Key: 
ABCD-EFGH-IJKL-MNOP 
 
Groups: 
['ABCD', 'EFGH', 'IJKL', 'MNOP'] 
 
Number of Groups: 4 
 
Total Letters: 16 
Total Vowels: 4 
 
Merged Key: 
ABCDEFGHIJKLMNOP 
 
License Key Status: Valid 
 
"""

#----------------------------------------------
# License Key Verification System
#----------------------------------------------

license_key = "ABCD-EFGH-IJKL-MNOP"

print("License Key:")
print(license_key)

#----------------------------------------------
# Create list of groups (Without split)
#----------------------------------------------

groups = []
group = ""

for ch in license_key:

    # If hyphen found, save current group
    if ch == "-":
        groups.append(group)
        group = ""

    else:
        group += ch

# Add last group
groups.append(group)

print("\nGroups:")
print(groups)

#----------------------------------------------
# Count Number of Groups
#----------------------------------------------

print("\nNumber of Groups:", len(groups))

#----------------------------------------------
# Verify there are exactly 4 groups
#----------------------------------------------

group_count_valid = False

if len(groups) == 4:
    group_count_valid = True

#----------------------------------------------
# Verify each group has 4 characters
#----------------------------------------------

group_length_valid = True

for g in groups:

    if len(g) != 4:
        group_length_valid = False

#----------------------------------------------
# Count Total Letters
#----------------------------------------------

letter_count = 0

for ch in license_key:

    if ch.isalpha():
        letter_count += 1

print("\nTotal Letters:", letter_count)

#----------------------------------------------
# Count Vowels
#----------------------------------------------

vowel_count = 0

vowels = "AEIOUaeiou"

for ch in license_key:

    if ch in vowels:
        vowel_count += 1

print("Total Vowels:", vowel_count)

#----------------------------------------------
# Remove Hyphens and Create Merged Key
#----------------------------------------------

merged_key = ""

for ch in license_key:

    if ch != "-":
        merged_key += ch

print("\nMerged Key:")
print(merged_key)

#----------------------------------------------
# Display Key Status
#----------------------------------------------

if group_count_valid and group_length_valid:
    print("\nLicense Key Status: Valid")
else:
    print("\nLicense Key Status: Invalid")