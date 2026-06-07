"""units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 450, 
    "House104": 290, 
    "House105": 150, 
    "House106": 510, 
    "House107": 220, 
    "House108": 390, 
    "House109": 170, 
    "House110": 260 
} 
Tasks 
• Display houses consuming more than 300 units.  
• Count houses consuming less than 200 units.  
• Find the house with the highest consumption.  
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units).  
• Categorize houses as:  
o Low: < 200 units  
o Medium: 200–350 units  
o High: > 350 units """
# Electricity consumption dictionary
# Key = House Number
# Value = Units Consumed

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# ==================================================
# 1. Display houses consuming more than 300 units
# ==================================================

print("Houses consuming more than 300 units:")

# Loop through each house and units
for house, consumption in units.items():

    # Check if consumption is greater than 300
    if consumption > 300:

        # Print house number
        print(house)

# ==================================================
# 2. Count houses consuming less than 200 units
# ==================================================

# Variable to store count
count = 0

# Loop through all unit values
for consumption in units.values():

    # Check if consumption is less than 200
    if consumption < 200:

        # Increase count by 1
        count += 1

# Display count
print("Houses consuming less than 200 units:", count)

# ==================================================
# 3. Find the house with the highest consumption
# ==================================================

# Variable to store house number
highest_house = ""

# Variable to store highest consumption
highest_consumption = 0

# Loop through each house and units
for house, consumption in units.items():

    # Check if current consumption is greater
    # than highest consumption
    if consumption > highest_consumption:

        # Update highest consumption
        highest_consumption = consumption

        # Store house number
        highest_house = house

# Display house with highest consumption
print("House with Highest Consumption:", highest_house)

# Display units consumed
print("Units:", highest_consumption)

# ==================================================
# 4. Create a list of houses eligible for
#    energy-saving awareness campaign
# ==================================================

# Empty list to store house numbers
campaign_list = []

# Loop through each house and units
for house, consumption in units.items():

    # Check if consumption is greater than 400
    if consumption > 400:

        # Add house to list
        campaign_list.append(house)

# Display list
print("Houses for Energy Saving Campaign:")
print(campaign_list)

# ==================================================
# 5. Categorize houses
# ==================================================

print("House Categories:")

# Loop through each house and units
for house, consumption in units.items():

    # Check if consumption is less than 200
    if consumption < 200:

        # Low category
        print(house, "-> Low")

    # Check if consumption is between 200 and 350
    elif consumption >= 200 and consumption <= 350:

        # Medium category
        print(house, "-> Medium")

    # Otherwise consumption is greater than 350
    else:

        # High category
        print(house, "-> High")