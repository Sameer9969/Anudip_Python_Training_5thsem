"""Problem 7: Smart Agriculture Crop Monitoring System 
Problem Statement 
Crop moisture levels (%) are stored as follows: 
moisture = { 
    "Field1": 55, 
    "Field2": 30, 
    "Field3": 72, 
    "Field4": 28, 
    "Field5": 64, 
    "Field6": 35, 
    "Field7": 80, 
    "Field8": 42, 
    "Field9": 25, 
    "Field10": 68 
} 
Tasks 
1. Identify fields requiring irrigation (< 40%).  
2. Classify fields into Low, Moderate, and High moisture categories.  
3. Count fields in each category.  
4. Find fields with the highest and lowest moisture levels.  
5. Generate an irrigation priority list.  
Sample Output 
Fields Requiring Irrigation: 
Field2 
Field4 
Field6 
Field9 
 
Low Moisture Fields: 
['Field2', 'Field4', 'Field6', 'Field9'] 
 
Moderate Moisture Fields: 
['Field1', 'Field5', 'Field8'] 
 
High Moisture Fields: 
['Field3', 'Field7', 'Field10'] 
 
Field with Highest Moisture: 
Field7 (80%) 
 
Field with Lowest Moisture: 
Field9 (25%) 
 
Irrigation Priority List: 
['Field9', 'Field4', 'Field2', 'Field6'] b"""

moisture = {
    "Field1": 55,
    "Field2": 30,
    "Field3": 72,
    "Field4": 28,
    "Field5": 64,
    "Field6": 35,
    "Field7": 80,
    "Field8": 42,
    "Field9": 25,
    "Field10": 68
}

# 1. Fields requiring irrigation
print("Fields Requiring Irrigation:")

irrigation = []

for field in moisture:
    if moisture[field] < 40:
        print(field)
        irrigation.append(field)

# 2. Classify fields
low = []
moderate = []
high = []

for field in moisture:
    if moisture[field] < 40:
        low.append(field)
    elif moisture[field] <= 65:
        moderate.append(field)
    else:
        high.append(field)

print("\nLow Moisture Fields:")
print(low)

print("\nModerate Moisture Fields:")
print(moderate)

print("\nHigh Moisture Fields:")
print(high)

# 3. Count fields in each category
print("\nNumber of Low Moisture Fields:", len(low))
print("Number of Moderate Moisture Fields:", len(moderate))
print("Number of High Moisture Fields:", len(high))

# 4. Highest and Lowest Moisture Fields
highest_field = max(moisture, key=moisture.get)
lowest_field = min(moisture, key=moisture.get)

print("\nField with Highest Moisture:")
print(highest_field, "(", moisture[highest_field], "% )")

print("\nField with Lowest Moisture:")
print(lowest_field, "(", moisture[lowest_field], "% )")

# 5. Irrigation Priority List
priority = sorted(irrigation, key=lambda x: moisture[x])

print("\nIrrigation Priority List:")
print(priority)