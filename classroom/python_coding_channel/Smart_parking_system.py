"""Problem 3: Smart Parking Management System 
Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.  
Sample Output 
Vacant Parking Slots: 
2 4 7 9 
Occupied Slots: 6 
Vacant Slots: 4 
Vehicle Allocated to Slot 2 
Occupancy Percentage: 70.0% 
Parking Details Saved Successfully."""

# Smart Parking Management System

# Parking slot data
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# 1. Display vacant parking slot numbers
print("Vacant Parking Slots:")

for i in range(len(parking_slots)):     # List ke har slot par loop
    if parking_slots[i] == "Vacant":    # Agar slot vacant hai
        print(i + 1, end=" ")           # Slot number print karo

print()

# 2. Count occupied and vacant slots
occupied = 0
vacant = 0

for slot in parking_slots:              # Har slot check karo
    if slot == "Occupied":
        occupied += 1
    else:
        vacant += 1

print("\nOccupied Slots:", occupied)
print("Vacant Slots:", vacant)

# 3. Allocate first vacant slot
for i in range(len(parking_slots)):     # Starting se slot check karo
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"   # Slot allocate kar do
        print("\nVehicle Allocated to Slot", i + 1)
        break                           # First vacant slot mil gaya

# 4. Calculate occupancy percentage
occupied_count = 0

for slot in parking_slots:
    if slot == "Occupied":
        occupied_count += 1

total_slots = len(parking_slots)

occupancy_percentage = (occupied_count / total_slots) * 100

print("Occupancy Percentage:", occupancy_percentage, "%")

# 5. Save updated parking information in file
file = open("parking.txt", "w")

for slot in parking_slots:
    file.write(slot + "\n")             # Har slot ki status file me likho

file.close()

print("Parking Details Saved Successfully.")