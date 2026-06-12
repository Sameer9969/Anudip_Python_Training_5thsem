"""Problem 1: Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate the total units consumed.  
5. Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).  
Sample Output 
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5 """

#==========================================
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
#===========================================
# 1. Display houses consuming more than 400 units.
#===========================================
print("Houses Consuming More Than 400 Units:")
for house in units:
    if units[house] > 400:
        print(house)
#===========================================
# 2. Find the highest-consuming house.
#===========================================
highest = 0
for house in units:
    if units[house] > highest:
        highest = units[house]
        highest_house = house
print("\nHighest Consumption:")
print(highest_house, "(", highest, "units)")
#============================================
# 3. Find the lowest-consuming house.
#============================================
lowest = float('inf')
for house in units:
    if units[house] < highest:
        lowest = units[house]
        Lowest_house = house
print("\nLowest Consumption:")
print(Lowest_house, "(", lowest, "units)")

#============================================
# 4. Calculate the total units consumed.
#============================================
total_consumned = 0
for house in units:
    total_consumned += units[house]
print("\nTotal Units Consumed:", total_consumned)
#============================================
# 5. Create separate lists for: 
#============================================
low = []
medium = []
high = []
for house in units:
    if units[house] < 200:
        low.append(house)
    elif units[house] <= 400:
        medium.append(house)
    else:
        high.append(house)
print("\nLow Consumption:", low)
print("\nMedium Consumption:", medium)
print("\nHigh Consumption:", high)
#============================================
# 6. Count houses eligible for an energy-saving campaign (consumption > 300).  
#============================================
count = 0
for house in units:
    if units[house] > 300:
        count += 1
print("\nEligible for Energy-Saving Campaign:", count)
#============================================

