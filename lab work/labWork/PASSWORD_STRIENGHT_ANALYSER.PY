"""2. Password Strength Analyzer 
Problem Statement 
A user enters a password. 
Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately.  
Sample Output 
Password: Python@2026! 
 
Uppercase Letters: 1 
Lowercase Letters: 5 
Digits: 4 
Special Characters: 2 
 
Digits Found: ['2', '0', '2', '6'] 
Special Characters Found: ['@', '!'] 
 
Password Strength: Strong"""
#----------------------------------------------
# 1. Minimum length 8
#----------------------------------------------
password = """Python@2026!"""

if len(password) < 8:
    print("Password Strength: Weak")
else:
    print("Password Strength: Strong")
#----------------------------------------------
# 2. Count lowercase letters.
#----------------------------------------------
count = 0
for char in password:
    if char.islower():
        count += 1
print("Lowercase Letters:", count)
#----------------------------------------------
# 3. Count digits
#----------------------------------------------
count = 0
for char in password:
    if char.isdigit():
        count += 1
print("Digits:", count)
#----------------------------------------------
# 4.Count special characters.
#----------------------------------------------
count = 0
for char in password:
    if not char.isalnum():
        count += 1
print("Special Characters:", count)
#----------------------------------------------
# 5.Display all digits separately.
#----------------------------------------------
digite = []
for char in password:
    if char.isdigit():
        digite.append(char)
print("Digits Found:", digite)
#----------------------------------------------
# 6.Display all special characters separately.
#----------------------------------------------
sepecial_char = []
for char in password:
    if not char.isalnum():
        sepecial_char.append(char)
print("Special Characters Found:", sepecial_char)
#----------------------------------------------