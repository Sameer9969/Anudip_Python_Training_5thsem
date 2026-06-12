"""Problem 6: Space Mission Telemetry Analyzer 
Problem Statement 
Sensor readings are stored in telemetry.txt. 
101 
98 
105 
110 
112 
95 
90 
88 
120 
102 
Tasks 
1. Read all sensor readings.  
2. Display abnormal readings (< 90 or > 110).  
3. Calculate average sensor value.  
4. Count normal and abnormal readings.  
5. Store abnormal readings in alerts.txt.  
Sample Output 
Abnormal Sensor Readings: 
88 
120 
 
Average Sensor Value: 
102.1 
 
Normal Readings: 8 
Abnormal Readings: 2 
 
Alert File Generated Successfully."""

# Read sensor readings from telemetry.txt

file = open("telemetry.txt", "r")

readings = []

for line in file:
    readings.append(int(line.strip()))

file.close()

# Display abnormal readings
print("Abnormal Sensor Readings:")

abnormal = []

for reading in readings:
    if reading < 90 or reading > 110:
        print(reading)
        abnormal.append(reading)

# Calculate average
total = 0

for reading in readings:
    total = total + reading

average = total / len(readings)

print("\nAverage Sensor Value:")
print(round(average, 1))

# Count normal and abnormal readings
normal_count = 0
abnormal_count = 0

for reading in readings:
    if reading < 90 or reading > 110:
        abnormal_count = abnormal_count + 1
    else:
        normal_count = normal_count + 1

print("\nNormal Readings:", normal_count)
print("Abnormal Readings:", abnormal_count)

# Store abnormal readings in alerts.txt
alert_file = open("alerts.txt", "w")

for reading in abnormal:
    alert_file.write(str(reading) + "\n")

alert_file.close()

print("\nAlert File Generated Successfully.")
###########################cd classroom\python_test3
############################ python cyber_security_login_audit.py