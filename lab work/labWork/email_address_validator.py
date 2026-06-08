"""6. Email Address Validator 
Problem Statement 
A user enters an email address: 
rahul.sharma2026@gmail.com 
Tasks 
Write a program to: 
1. Extract username.  
2. Extract domain name.  
3. Extract extension.  
4. Count digits present in username.  
5. Count special characters.  
6. Check whether:  
o Exactly one '@' exists.  
o At least one '.' exists after '@'.  
7. Display Valid Email or Invalid Email.  
Sample Output 
Email: rahul.sharma2026@gmail.com 
 
Username: rahul.sharma2026 
Domain: gmail 
Extension: com 
 
Digits Found: 4 
Special Characters Found: 2 
 
Email Status: Valid"""

#----------------------------------------------
# Email Address Validator
#----------------------------------------------

email = "rahul.sharma2026@gmail.com"

print("Email:", email)

#----------------------------------------------
# 1. Extract Username
#----------------------------------------------
at_index = email.index("@")

username = email[:at_index]

print("\nUsername:", username)

#----------------------------------------------
# 2. Extract Domain Name
#----------------------------------------------
dot_index = email.rindex(".")

domain = email[at_index + 1 : dot_index]

print("Domain:", domain)

#----------------------------------------------
# 3. Extract Extension
#----------------------------------------------
extension = email[dot_index + 1:]

print("Extension:", extension)

#----------------------------------------------
# 4. Count Digits in Username
#----------------------------------------------
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

print("\nDigits Found:", digit_count)

#----------------------------------------------
# 5. Count Special Characters
#----------------------------------------------
special_count = 0

for ch in email:
    if not ch.isalnum():
        special_count += 1

print("Special Characters Found:", special_count)

#----------------------------------------------
# 6 & 7. Validate Email
#----------------------------------------------

at_count = 0

for ch in email:
    if ch == "@":
        at_count += 1

if at_count == 1 and "." in email[at_index:]:
    print("\nEmail Status: Valid")
else:
    print("\nEmail Status: Invalid")