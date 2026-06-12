"""Problem 9: Hospital Patient Monitoring System 
Problem Statement 
Patient heart rates are recorded below. 
Sample Data 
heart_rate = { 
    "P101": 72, 
    "P102": 105, 
    "P103": 88, 
    "P104": 120, 
    "P105": 65, 
    "P106": 98, 
    "P107": 110, 
    "P108": 70, 
    "P109": 85, 
    "P110": 130 
} 
Tasks 
1. Display critical patients (heart rate >100).  
2. Find highest and lowest heart rate.  
3. Calculate average heart rate.  
4. Count stable patients (60–100 bpm).  
Sample Output 
Critical Patients: 
P102 
P104 
P107 
P110 
 
Highest Heart Rate: 
P110 (130 bpm) 
 
Lowest Heart Rate: 
P105 (65 bpm) 
 
Average Heart Rate: 94.3 bpm 
 
Stable Patients: 6"""


heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70
}

# 1. Display Critical Patients
print("Critical Patients:")
for patient in heart_rate:
    if heart_rate[patient] > 100:
        print(patient)

# 2. Find Highest Heart Rate
highest_patient = ""
highest_rate = 0

for patient in heart_rate:
    if heart_rate[patient] > highest_rate:
        highest_rate = heart_rate[patient]
        highest_patient = patient

print("\nHighest Heart Rate:")
print(highest_patient, "(", highest_rate, "bpm )")

# 3. Find Lowest Heart Rate
first = True

for patient in heart_rate:
    if first:
        lowest_rate = heart_rate[patient]
        lowest_patient = patient
        first = False
    elif heart_rate[patient] < lowest_rate:
        lowest_rate = heart_rate[patient]
        lowest_patient = patient

print("\nLowest Heart Rate:")
print(lowest_patient, "(", lowest_rate, "bpm )")

# 4. Calculate Average Heart Rate
total = 0
count = 0

for rate in heart_rate.values():
    total = total + rate
    count = count + 1

average = total / count

print("\nAverage Heart Rate:")
print(round(average, 1), "bpm")

# 5. Count Stable Patients (60–100 bpm)
stable_count = 0

for rate in heart_rate.values():
    if rate >= 60 and rate <= 100:
        stable_count = stable_count + 1

print("\nStable Patients:", stable_count)
