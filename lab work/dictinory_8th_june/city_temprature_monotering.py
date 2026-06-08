"""3. City Temperature Monitoring System 
Problem Statement 
Daily temperatures of different cities are stored as: 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C.  
Sample Output 
Cities Above 40°C: 
Delhi 
Jaipur 
Ahmedabad 
 
Hottest City: Ahmedabad (43°C) 
 
Coolest City: Bengaluru (28°C) 
 
Average Temperature: 36.8°C 
 
Pleasant Cities: 
['Mumbai', 'Bengaluru', 'Pune'] 
 
Cities Between 35°C and 40°C: 4"""
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
}
#==========================================
# 1. Display cities having temperature above 40°C.
#==========================================

for city, temperatures in temperature.items():
    if temperatures > 40:
        print(city)
#==========================================
# 2. Find the hottest city.
#==========================================
hottest = None
hottest_temp = 0
for city, temp in temperature.items():
    if temp > hottest_temp:
        hottest = city
        hottest_temp = temp
print("Hottest City: ",hottest,"(",hottest_temp,")")
#==========================================
# 3. Find the coolest city.
#==========================================
coolest = None
coolest_temp = float('inf')
for city, temp in temperature.items():
    if temp < coolest_temp:
        coolest = city
        coolest_temp = temp
print("Coolest City: ",coolest,"(",coolest_temp,")")
#==========================================
# 4. Calculate average temperature.
#==========================================
total_temp = 0
for temp in temperature.values():
    total_temp += temp
average_temp = total_temp / len(temperature)
print("Average Temperature: ",average_temp)
#==========================================
# 5. Create a list of pleasant cities (temperature < 35°
#==========================================
pleasant = []
for city, temp in temperature.items():
    if temp < 35:
        pleasant.append(city)
print("Pleasant Cities: ")
print(pleasant)
#==========================================
# 6. Count cities with temperature between 35°C and 40°C.
#================================
count = 0
for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1
print("Cities Between 35°C and 40°C: ",count)
#==========================================