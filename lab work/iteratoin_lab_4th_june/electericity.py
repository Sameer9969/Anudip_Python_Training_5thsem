# 5. Electricity Bill Calculator 
# Problem Statement: 
# Calculate electricity bill based on the following slab rates: 
# Units Rate 
# 0-100 ₹5/unit 
# 101-200 ₹7/unit 
# Above 200 ₹10/unit 
# Display: 
# • Units Consumed  
# • Total Bill  
# • Category (Low / Medium / High Consumption) 
# Program to calculate Electricity Bill using Slabs

# Take number of units consumed from user
units = int(input("Enter electricity units consumed: "))

# Initialize bill amount
bill = 0

# Calculate bill according to slabs

# For first 100 units
if units <= 100:
    bill = units * 5

# For units between 101 and 200
elif units <= 200:
    # First 100 units at ₹5/unit
    bill = (100 * 5)

    # Remaining units at ₹7/unit
    bill += (units - 100) * 7

# For units above 200
else:
    # First 100 units at ₹5/unit
    bill = (100 * 5)

    # Next 100 units at ₹7/unit
    bill += (100 * 7)

    # Remaining units above 200 at ₹10/unit
    bill += (units - 200) * 10


# Display final bill amount
print("Final Payable Amount = ₹", bill)