"""1. Railway Reservation Seat Analyzer 
Problem Statement 
A railway coach has seats represented as follows: 
seats = [ 
    "Booked", "Available", "Booked", "Booked", 
    "Available", "Available", "Booked", "Available", 
    "Booked", "Booked", "Available", "Booked" 
] 
Requirements 
Create the following functions: 
1. count_seats(seats) 
Returns the number of booked and available seats. 
2. first_available(seats) 
Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) 
Returns the percentage of occupied seats. 
4. display_available_seats(seats) 
Displays all available seat numbers. 
Sample Output 
Booked Seats: 7 
Available Seats: 5 

First Available Seat: 2 

Occupancy Percentage: 58.33% 

Available Seat Numbers: 
2 5 6 8 11 """

seats = [ 
    "Booked", "Available", "Booked", "Booked", 
    "Available", "Available", "Booked", "Available", 
    "Booked", "Booked", "Available", "Booked" 
] 

#==========================================
#1. count_seats(seats)
#==========================================
def count_seats(seats):
    booked_count = 0
    available_count = 0
    for seat in seats:
        if seat == "Booked":
            booked_count += 1
            
        else:
            available_count += 1
            
    return booked_count, available_count
#============================================
# 2.first_available(seats) 
#============================================
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1
#============================================
# 3. occupancy_percentage(seats)
#============================================
def occupancy_percentage(seats):
    booked_count, available_count = count_seats(seats)
    total_seats = len(seats)
    percentage = (booked_count / total_seats) * 100
    return percentage
#============================================
# 4. display_available_seats(seats)
#============================================
def display_available_seats(seats):
    print("Available Seat Numbers:")
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1)
#============================================
# function call
booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("\nOccupancy Percentage:", occupancy_percentage(seats), "%")


display_available_seats(seats)