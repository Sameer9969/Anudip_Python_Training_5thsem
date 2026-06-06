'''Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
• 1 = Occupied  
• 0 = Available  
Write a program to: 
• Count occupied and available slots.  
• Find the first available slot.  
• Display all available slot numbers.  
• Check whether parking occupancy exceeds 75%. '''
slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Count occupied and available
occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# Find the first available slot
first_available = 1
for i in range(len(slots)):
    if slots[i] == 0:
        first_available = i
        break

if first_available != -1:
    print("First Available Slot:", first_available + 1)
else:
    print("No Available Slots")

# Display all available slot numbers
print("Available Slot Numbers:")
for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)

# Check occupancy percentage
total_slots = len(slots)
occupancy_percentage = (occupied / total_slots) * 100

if (occupancy_percentage > 75):
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy is within acceptable range")

