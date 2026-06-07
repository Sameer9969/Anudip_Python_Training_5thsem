"""Sample Data 
passengers = { 
    "Stop1": 12, 
    "Stop2": 25, 
    "Stop3": 18, 
    "Stop4": 32, 
    "Stop5": 9, 
    "Stop6": 28, 
    "Stop7": 14, 
    "Stop8": 7, 
    "Stop9": 21, 
    "Stop10": 16 
} 
Tasks 
• Display stops having more than 20 passengers.  
• Count stops with fewer than 10 passengers.  
• Find the busiest stop.  
• Create a list of stops requiring an extra bus (passengers > 25).  
• Calculate the average number of passengers. """

# Bus passenger dictionary
# Key = Bus Stop Name
# Value = Number of Passengers

passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# ==================================================
# 1. Display stops having more than 20 passengers
# ==================================================

print("Stops having more than 20 passengers:")

# Loop through each stop and passenger count
for stop, count in passengers.items():

    # Check if passenger count is greater than 20
    if count > 20:

        # Print stop name
        print(stop)

# ==================================================
# 2. Count stops with fewer than 10 passengers
# ==================================================

# Variable to store count
low_passenger_count = 0

# Loop through all passenger counts
for count in passengers.values():

    # Check if passengers are less than 10
    if count < 10:

        # Increase count by 1
        low_passenger_count += 1

# Display total count
print("Stops with fewer than 10 passengers:", low_passenger_count)

# ==================================================
# 3. Find the busiest stop
# ==================================================

# Variable to store busiest stop name
busiest_stop = ""

# Variable to store maximum passengers
max_passengers = 0

# Loop through each stop and passenger count
for stop, count in passengers.items():

    # Check if current passenger count is greater
    # than the maximum passengers found so far
    if count > max_passengers:

        # Update maximum passenger count
        max_passengers = count

        # Store stop name
        busiest_stop = stop

# Display busiest stop
print("Busiest Stop:", busiest_stop)

# Display passenger count
print("Passengers:", max_passengers)

# ==================================================
# 4. Create a list of stops requiring an extra bus
# ==================================================

# Empty list to store stop names
extra_bus_stops = []

# Loop through each stop and passenger count
for stop, count in passengers.items():

    # Check if passengers are more than 25
    if count > 25:

        # Add stop name to list
        extra_bus_stops.append(stop)

# Display list
print("Stops requiring an extra bus:")
print(extra_bus_stops)

# ==================================================
# 5. Calculate the average number of passengers
# ==================================================

# Variable to store total passengers
total_passengers = 0

# Loop through all passenger counts
for count in passengers.values():

    # Add current passenger count to total
    total_passengers += count

# Find total number of stops
total_stops = len(passengers)

# Calculate average passengers
average_passengers = total_passengers / total_stops

# Display average
print("Average Number of Passengers:", average_passengers)
