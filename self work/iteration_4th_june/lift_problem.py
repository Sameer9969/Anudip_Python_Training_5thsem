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

# Lift starts at floor 0
current_floor = 0

# Total floors travelled
total_travel = 0

while True:
    # Take destination floor from user
    dest = int(input("Enter destination floor (-1 to stop): "))

    # Stop condition
    if dest == -1:
        break

    # If going up or down, calculate distance
    travel = dest - current_floor

    # If negative, make it positive (distance can't be negative)
    if travel < 0:
        travel = -travel

    # Show floors travelled in this trip
    print("Travelled:", travel, "floors")

    # Add to total travel
    total_travel = total_travel + travel

    # Update current floor
    current_floor = dest

# Final result
print("Total Travelled:", total_travel, "floors")
print("------------------------------")