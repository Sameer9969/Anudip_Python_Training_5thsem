"""Problem 8: Smart Water Consumption Monitoring System 
Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data 
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
o Low (<2000 litres)  
o Medium (2000–3500 litres)  
o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres).  
Sample Output 
Houses Consuming More Than 3000 Litres: 
House103 
House106 
House108 
House110 
 
Highest Consumption: 
House110 (4500 litres) 
 
Lowest Consumption: 
House109 (1500 litres) 
 
Total Consumption: 28,300 litres 
 
Low Consumption: 
['House101', 'House105', 'House109'] 
 
Medium Consumption: 
['House102', 'House103', 'House104', 'House107'] 
 
High Consumption: 
['House106', 'House108', 'House110'] 
 
Eligible Households: 5"""

water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
#==========================================
# 1. Display houses consuming more than 3000 litres.
#==========================================
print("Houses Consuming More Than 3000 Litres:")
for house in water_usage:
    if water_usage[house] > 3000:
        print(house)
#===========================================
# 2. Find the highest and lowest consumers.
#===========================================
highest = 0
lowest = float('inf')

for house in water_usage:
    if water_usage[house] > highest:
        highest = water_usage[house]
        highest_house = house

    if water_usage[house] < lowest:
        lowest = water_usage[house]
        lowest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest, "litres)")

print("\nLowest Consumption:")
print(lowest_house, "(", lowest, "litres)")
#===========================================
# 3. Calculate total water consumption.
#===========================================
total = 0
for house in water_usage:
    total += water_usage[house]

print("\nTotal Consumption:", total, "litres")
#===========================================
# 4. Categorize houses: 
#===========================================
low = []
medium = []
high = []

for house in water_usage:
    if water_usage[house] < 2000:
        low.append(house)
    elif water_usage[house] <=1000:
        medium.append(house)
    else:
        high.append(house)

print("\nLow Consumption:", low)
print("\nMedium Consumption:", medium)
print("\nHigh Consumption:", high)
#===========================================
