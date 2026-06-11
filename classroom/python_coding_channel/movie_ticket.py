"""Problem 7: Movie Ticket Booking System 
Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage.  
Sample Output 
Available Seats: 
A2 
A4 
B2 
B4 
C2 
 
Booked Seats: 5 
Available Seats: 5 
 
Seat A2 Reserved Successfully. 
 
Hall Occupancy Percentage: 60.0% 
 
Booking Details Saved Successfully."""

# Movie Ticket Booking System

tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

# Display available seats
print("Available Seats:")

for seat in tickets:
    if tickets[seat] == "Available":
        print(seat)

# Count booked and available seats
booked = 0
available = 0

for seat in tickets:
    if tickets[seat] == "Booked":
        booked += 1
    else:
        available += 1

print("\nBooked Seats:", booked)
print("Available Seats:", available)

# Reserve first available seat
for seat in tickets:
    if tickets[seat] == "Available":
        tickets[seat] = "Booked"
        print("\nSeat", seat, "Reserved Successfully.")
        break

# Recalculate booked seats after reservation
booked = 0

for seat in tickets:
    if tickets[seat] == "Booked":
        booked += 1

# Calculate hall occupancy percentage
total_seats = len(tickets)
occupancy = (booked / total_seats) * 100

print("\nHall Occupancy Percentage:", occupancy, "%")

# Save updated booking details to file
file = open("tickets.txt", "w")

for seat in tickets:
    file.write(seat + "," + tickets[seat] + "\n")

file.close()

print("\nBooking Details Saved Successfully.")