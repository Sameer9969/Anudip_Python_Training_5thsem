"""Assignment 2: Email Validation & Domain Analytics System 
Problem Statement 
An organization has collected 20 email addresses from users. 
Create a program to analyze these email addresses. 
Requirements 
For each email: 
1. Extract username.  
2. Extract domain.  
3. Extract extension.  
4. Count digits in username.  
5. Count special characters.  
6. Check if email is valid:  
o Exactly one '@'  
o Contains '.'  
o No spaces  
7. Display invalid emails.  
8. Count emails belonging to each domain.  
Sample Input 
rahul123@gmail.com 
priya@outlook.com 
anuj@company.in 
Challenge 
Generate a domain report: 
gmail.com     -> 8 users 
outlook.com   -> 5 users 
yahoo.com     -> 3 users 
company.in    -> 4 users """


# ==========================================
# Email Validation & Domain Analytics System
# ==========================================

# Total emails to analyze
total_emails = 20

# Dictionary for domain count
domain_report = {}

# List to store invalid emails
invalid_emails = []

# ------------------------------------------
# Loop for taking 20 email addresses
# ------------------------------------------
for i in range(total_emails):

    print("\n================================")
    print("Email", i + 1)
    print("================================")

    email = input("Enter Email Address: ")

    # --------------------------------------
    # Check Email Validity
    # Conditions:
    # 1. Exactly one '@'
    # 2. Contains '.'
    # 3. No spaces
    # --------------------------------------

    valid = True

    if email.count("@") != 1:
        valid = False

    if "." not in email:
        valid = False

    if " " in email:
        valid = False

    # --------------------------------------
    # If email is valid
    # --------------------------------------
    if valid:

        # Split email into username and domain
        parts = email.split("@")

        username = parts[0]
        domain = parts[1]

        # ----------------------------------
        # Extract extension
        # Example:
        # gmail.com -> com
        # company.in -> in
        # ----------------------------------
        domain_parts = domain.split(".")
        extension = domain_parts[-1]

        # ----------------------------------
        # Count digits in username
        # ----------------------------------
        digit_count = 0

        for ch in username:
            if ch.isdigit():
                digit_count += 1

        # ----------------------------------
        # Count special characters
        # in username
        # ----------------------------------
        special_count = 0

        for ch in username:

            if not ch.isalnum():
                special_count += 1

        # ----------------------------------
        # Store domain count
        # ----------------------------------
        if domain in domain_report:
            domain_report[domain] += 1
        else:
            domain_report[domain] = 1

        # ----------------------------------
        # Display email analysis
        # ----------------------------------
        print("\n------ Email Analysis ------")

        print("Username           :", username)
        print("Domain             :", domain)
        print("Extension          :", extension)
        print("Digits in Username :", digit_count)
        print("Special Characters :", special_count)
        print("Email Status       : Valid")

    # --------------------------------------
    # If email is invalid
    # --------------------------------------
    else:

        invalid_emails.append(email)

        print("\n------ Email Analysis ------")
        print("Email Status : Invalid")

# ==========================================
# Display Invalid Emails
# ==========================================

print("\n\n================================")
print("INVALID EMAILS")
print("================================")

if len(invalid_emails) > 0:

    for email in invalid_emails:
        print(email)

else:
    print("No Invalid Emails Found")

# ==========================================
# Domain Report
# ==========================================

print("\n\n================================")
print("DOMAIN REPORT")
print("================================")

for domain in domain_report:
    print(domain, "->", domain_report[domain], "users")

# ==========================================
# Final Summary
# ==========================================

print("\n================================")
print("FINAL REPORT")
print("================================")

print("Total Emails Analyzed :", total_emails)
print("Valid Emails          :", total_emails - len(invalid_emails))
print("Invalid Emails        :", len(invalid_emails))