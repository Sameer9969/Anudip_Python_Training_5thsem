"""Problem 15: Function-Based Temperature Converter 
Problem Statement 
Daily temperatures recorded in Celsius are given below. 
Sample Data 
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31] 
Tasks 
Create functions to: 
1. Convert Celsius to Fahrenheit.  
2. Display all temperatures in Fahrenheit.  
3. Find the highest Fahrenheit temperature.  
4. Find the lowest Fahrenheit temperature.  
5. Calculate the average Fahrenheit temperature.  
Sample Output 
Temperatures in Fahrenheit: 
77.0 
86.0 
95.0 
104.0 
82.4 
89.6 
100.4 
71.6 
80.6 
87.8 
Highest Temperature: 104.0°F 
Lowest Temperature: 71.6°F 
A company wants to maintain backups of important documents. Create a program to copy the contents of 
one file into another. 
Average Temperature: 87.14°F"""

#=================================
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31] 
#=================================
# 1. Convert Celsius to Fahrenheit.
#=================================
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print("Temperatures in Fahrenheit:" )
#=================================
# 2. Display all temperatures in Fahrenheit.
#=================================
print("Temperatures in Fahrenheit:")
for temperature in temperatures:
    fahrenheit = celsius_to_fahrenheit(temperature)
    print(fahrenheit)
#================================
# 3. Find the highest Fahrenheit temperature.
#================================   
heigest = ""
for temperature in temperatures:
    fahrenheit = celsius_to_fahrenheit(temperature)
    if heigest == "":
        heigest = fahrenheit
    elif fahrenheit > heigest:
        heigest = fahrenheit
print("\nHighest Temperature:", heigest, "°F")
#================================
#4. Find the lowest Fahrenheit temperature.
#================================
lowest = ""
for temperature in temperatures:
    fahrenheit = celsius_to_fahrenheit(temperature)
    if lowest == "":
        lowest = fahrenheit
    elif fahrenheit < lowest:
        lowest = fahrenheit
print("\nLowest Temperature:", lowest, "°F")
#================================
# 5. Calculate the average Fahrenheit temperature.
#================================
total = 0
for temperature in temperatures:
    fahrenheit = celsius_to_fahrenheit(temperature)
    total += fahrenheit
average = total / len(temperatures)
print("\nAverage Temperature:", average, "°F")
#================================
