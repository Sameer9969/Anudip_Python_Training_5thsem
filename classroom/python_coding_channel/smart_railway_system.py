"""Problem 1: Smart Railway Reservation System 
Problem Statement 
A railway reservation system stores the booking status of seats in a train coach. 
Sample Data 
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
Tasks 
1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt.  
6. Display occupancy percentage.  
Sample Output 
Available Seats: 
2 4 7 9 
 
Booked Seats: 6 
Available Seats: 4 
 
Seat 2 Reserved Successfully. 
 
Occupancy Percentage: 70.0% 
 
Reservation Details Saved Successfully."""



seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
#==========================================
# 1. Display all available seat numbers. 
#==========================================
print("Available Seats: ")
for seat in seats: 
    if seats[seat] == "Available": 
        print(seat, end=" ") 
print()

#==========================================
# 2. Count booked and available seats.
#==========================================
booked = 0 
available = 0 
for seat in seats: 
    if seats[seat] == "Booked": 
        booked += 1 
    else: 
        available += 1 
print(f"Booked Seats: {booked}") 
print(f"Available Seats: {available}")

#======================================
# 3. Reserve the first available seat.
#======================================
print()
for seat in seats: 
    if seats[seat] == "Available": 
        seats[seat] = "Booked" 
        print(f"Seat {seat} Reserved Successfully.") 
        break 

#========================================
# 4.Cancel booking for a given seat number.
#========================================
for seat in seats: 
    if seats[seat] == "Booked": 
        seats[seat] = "Available" 
        print(f"Seat {seat} Cancelled Successfully.") 
        break 

#=========================================
# 5. Store the updated reservation status in reservations.txt.
#=========================================
with open("reservations.txt", "w") as file: 
    for seat in seats: 
        file.write(f"{seat}: {seats[seat]}\n") 
print("Reservation Details Saved Successfully.")

#=========================================
# 6. Display occupancy percentage.
#=========================================
total_seats = len(seats) 
booked_seats = total_seats - available 
occupancy_percentage = (booked_seats / total_seats) * 100 
print(f"Occupancy Percentage: {occupancy_percentage:.1f}%")


