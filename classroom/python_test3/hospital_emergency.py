"""Problem 8: Hospital Emergency Triage System 
Problem Statement 
Patients arriving at the emergency ward are categorized as: 
patients = [ 
    ("P101", "Critical"), 
    ("P102", "Stable"), 
    ("P103", "Critical"), 
    ("P104", "Moderate"), 
    ("P105", "Stable"), 
    ("P106", "Critical"), 
    ("P107", "Moderate"), 
    ("P108", "Stable"), 
    ("P109", "Critical"), 
    ("P110", "Moderate") 
] 
Tasks 
1. Count patients in each category.  
2. Display IDs of critical patients.  
3. Create separate lists for Critical, Moderate, and Stable patients.  
4. Determine which category requires maximum attention.  
5. Save critical patient IDs to critical_patients.txt.  
Sample Output 
Patient Count by Category: 
Critical : 4 
Moderate : 3 
Stable : 3 
 
Critical Patients: 
P101 
P103 
P106 
P109 
 
Critical Patients List: 
['P101', 'P103', 'P106', 'P109'] 
 
Moderate Patients List: 
['P104', 'P107', 'P110'] 
 
Stable Patients List: 
['P102', 'P105', 'P108'] 
 
Category Requiring Maximum Attention: 
Critical 
 
Critical Patient Report Generated Successfully."""

patients = [
    ("P101", "Critical"),
    ("P102", "Stable"),
    ("P103", "Critical"),
    ("P104", "Moderate"),
    ("P105", "Stable"),
    ("P106", "Critical"),
    ("P107", "Moderate"),
    ("P108", "Stable"),
    ("P109", "Critical"),
    ("P110", "Moderate")
]

# Create separate lists
critical = []
moderate = []
stable = []

# Count patients in each category
for patient in patients:
    if patient[1] == "Critical":
        critical.append(patient[0])
    elif patient[1] == "Moderate":
        moderate.append(patient[0])
    else:
        stable.append(patient[0])

# Display counts
print("Patient Count by Category:")
print("Critical :", len(critical))
print("Moderate :", len(moderate))
print("Stable :", len(stable))

# Display critical patient IDs
print("\nCritical Patients:")
for pid in critical:
    print(pid)

# Display lists
print("\nCritical Patients List:")
print(critical)

print("\nModerate Patients List:")
print(moderate)

print("\nStable Patients List:")
print(stable)

# Determine category requiring maximum attention
if len(critical) >= len(moderate) and len(critical) >= len(stable):
    attention = "Critical"
elif len(moderate) >= len(stable):
    attention = "Moderate"
else:
    attention = "Stable"

print("\nCategory Requiring Maximum Attention:")
print(attention)

# Save critical patient IDs to file
file = open("critical_patients.txt", "w")

for pid in critical:
    file.write(pid + "\n")

file.close()

print("\nCritical Patient Report Generated Successfully.")
###########################cd classroom\python_test3
############################ python cyber_security_login_audit.py