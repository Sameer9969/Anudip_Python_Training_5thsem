# Input lap times of N racers. 
# Display: 
# • Fastest racer position  
# • Slowest racer position  
# • Difference between fastest and slowest lap time
#number of racer jo race karege
n = int(input("Enter number of racers: "))
#faztest and  slowest ki value ko infinity let kar lege
fastest_time = float('inf')
slowest_time = float('-inf')
#looop n ke equal chalega
for i in range(1, n+1):
    lap_time = float(input("Enter lap time: "))
#comperision and finding position
    if lap_time < fastest_time:
        fastest_time = lap_time
        fastest_pos = i

    if lap_time > slowest_time:
        slowest_time = lap_time
        slowest_pos = i

difference = slowest_time - fastest_time

print("Fastest racer position =", fastest_pos)
print("Slowest racer position =", slowest_pos)
print("Difference =", difference)