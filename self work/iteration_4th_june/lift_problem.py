# Problem Statement: 
# A lift starts at floor 0. 
# The user repeatedly enters destination floors. 
# Display: 
# • Floors travelled in each trip  
# • Total floors travelled  
# • Stop when user enters -1  
# Example: 
# Current Floor: 0 
# Enter Destination: 5 
 
# Travelled: 5 floors 
 
# Enter Destination: 2 
 
# Travelled: 3 floors 
 
# Total Travelled: 8 floors

current_floor = 0
total_travel = 0

while True:
    dest = int(input("Enter destination floor (-1 to stop): "))

    if dest == -1:
        break

    travel = abs(dest - current_floor)

    print("Travelled:", travel, "floors")

    total_travel += travel
    current_floor = dest

print("Total Travelled:", total_travel, "floors")