# A bus has seats represented as: 
# seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
# Where: 
# • 1 → Seat Booked  
# • 0 → Seat Available  
# Write a program to: 
# 1. Count booked and available seats.  
# 2. Find the first available seat and stop searching immediately.  
# 3. Create a list of all available seat numbers.  
# 4. Determine whether the bus is more than 70% occupied.  
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0

available_seat = []

# Count booked and available seats
for seat in seats:
    if seat == 1: 
        booked += 1
    else:
        available += 1

# Find first available seat
for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1
        break

# Create list of available seat numbers
for i in range(len(seats)):
    if seats[i] == 0:
        available_seat.append(i + 1)

# Occupancy Percentage
occupancy = (booked * 100) / len(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seat)
print("Bus Occupancy:", occupancy, "%")

if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")
