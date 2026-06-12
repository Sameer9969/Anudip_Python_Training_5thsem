"""Problem 10: Smart Traffic Signal Optimization System 
Problem Statement 
Vehicle counts recorded at a junction every 15 minutes are stored as follows: 
traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85] 
Tasks 
1. Classify traffic conditions:  
o Low (< 80 vehicles)  
o Moderate (80–150 vehicles)  
o High (> 150 vehicles)  
2. Count occurrences of each traffic condition.  
3. Find the peak traffic interval.  
4. Create separate lists for each traffic category.  
5. Recommend whether manual traffic control is required (more than 3 High traffic intervals).  
Sample Output 
Traffic Conditions: 
120 → Moderate 
95 → Moderate 
140 → Moderate 
180 → High 
75 → Low 
60 → Low 
200 → High 
160 → High 
110 → Moderate 
85 → Moderate 
 
Low Traffic Intervals: 2 
Moderate Traffic Intervals: 5 
High Traffic Intervals: 3 
 
Peak Traffic Count: 
200 vehicles 
 
Low Traffic List: 
[75, 60] 
 
Moderate Traffic List: 
[120, 95, 140, 110, 85] 
 
High Traffic List: 
[180, 200, 160] 
 
Manual Traffic Control Required: 
No 
 
"""

traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85]

# Lists for different traffic categories
low = []
moderate = []
high = []

print("Traffic Conditions:")

# Classify traffic conditions
for count in traffic:
    if count < 80:
        print(count, "→ Low")
        low.append(count)
    elif count <= 150:
        print(count, "→ Moderate")
        moderate.append(count)
    else:
        print(count, "→ High")
        high.append(count)

# Count occurrences
print("\nLow Traffic Intervals:", len(low))
print("Moderate Traffic Intervals:", len(moderate))
print("High Traffic Intervals:", len(high))

# Peak traffic interval
peak = max(traffic)

print("\nPeak Traffic Count:")
print(peak, "vehicles")

# Display lists
print("\nLow Traffic List:")
print(low)

print("\nModerate Traffic List:")
print(moderate)

print("\nHigh Traffic List:")
print(high)

# Manual traffic control recommendation
print("\nManual Traffic Control Required:")

if len(high) > 3:
    print("Yes")
else:
    print("No")