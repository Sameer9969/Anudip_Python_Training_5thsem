"""Problem 8: City Temperature Monitoring System 
Problem Statement 
Daily temperatures of different cities are stored below. 
Sample Data 
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
1. Display cities with temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (<35°C).  
Sample Output 
Cities Above 40°C: 
Delhi 
Jaipur 
Ahmedabad 
 
Hottest City: 
Ahmedabad (43°C) 
 
Coolest City: 
Bengaluru (28°C) 
 
Average Temperature: 36.8°C 
 
Pleasant Cities: 
['Mumbai', 'Bengaluru', 'Pune']"""


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

# 1. Cities with temperature above 40°C
print("Cities Above 40°C:")
for city in temperature:
    if temperature[city] > 40:
        print(city)

# 2. Hottest city
hottest_city = ""
highest_temp = 0

for city in temperature:
    if temperature[city] > highest_temp:
        highest_temp = temperature[city]
        hottest_city = city

print("\nHottest City:")
print(hottest_city, "(", highest_temp, "°C )")

# 3. Coolest city
city_list = list(temperature.keys())

coolest_city = city_list[0]
lowest_temp = temperature[coolest_city]

for city in temperature:
    if temperature[city] < lowest_temp:
        lowest_temp = temperature[city]
        coolest_city = city

print("\nCoolest City:")
print(coolest_city, "(", lowest_temp, "°C )")

# 4. Average temperature
total = 0

for city in temperature:
    total = total + temperature[city]

average = total / len(temperature)

print("\nAverage Temperature:")
print(average, "°C")

# 5. Pleasant cities (<35°C)
print("\nPleasant Cities:")

for city in temperature:
    if temperature[city] < 35:
        print(city)
