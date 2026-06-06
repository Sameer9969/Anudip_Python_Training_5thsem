"""Passenger count at each stop: 
passengers = [12, 18, 25, 30, 28, 15, 8] 
Write a program to: 
• Find the busiest stop.  
• Display stops with fewer than 10 passengers.  
• Calculate average passengers.  
• Determine whether any stop exceeded 25 passengers. """

passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
max_passengers = passengers[0]
busiest_stop = 1

stop_number = 1

for passenger in passengers:
    if passenger > max_passengers:
        max_passengers = passenger
        busiest_stop = stop_number

    stop_number += 1

print("Busiest Stop:", busiest_stop)
print("Passengers:", max_passengers)

# Stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")

stop_number = 1

for passenger in passengers:
    if passenger < 10:
        print("Stop", stop_number)

    stop_number += 1

# Average passengers
total = 0

for passenger in passengers:
    total += passenger

average = total / len(passengers)

print("\nAverage Passengers:", average)

# Check if any stop exceeded 25 passengers
found = False

for passenger in passengers:
    if passenger > 25:
        found = True
        break

if found:
    print("\nA stop exceeded 25 passengers")
else:
    print("\nNo stop exceeded 25 passengers")