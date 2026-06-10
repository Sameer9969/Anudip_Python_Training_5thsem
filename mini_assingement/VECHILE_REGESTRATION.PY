"""Assignment 4: Vehicle Registration Verification System 
Problem Statement 
A transport department wants to verify vehicle registration numbers. 
Store at least 20 vehicle numbers. 
Example 
MH12AB4589 
DL05XY9988 
KA03PQ1234 
Requirements 
For each registration number: 
1. Extract state code.  
2. Extract district code.  
3. Extract series.  
4. Extract vehicle number.  
5. Count letters and digits.  
6. Validate format:  
o First 2 characters = Alphabets  
o Next 2 characters = Digits  
o Next 2 characters = Alphabets  
o Last 4 characters = Digits  
7. Display invalid registrations.  
8. Count vehicles state-wise.  
Challenge 
Generate a state-wise report: 
MH -> 6 Vehicles 
DL -> 4 Vehicles 
KA -> 5 Vehicles 
UP -> 5 Vehicles """

# ==========================================
# Vehicle Registration Verification System
# Beginner Friendly Program
# ==========================================

# Store at least 20 vehicle registration numbers

vehicles = [
    "MH12AB4589",
    "DL05XY9988",
    "KA03PQ1234",
    "UP14CD5678",
    "MH20EF3456",
    "DL07GH7890",
    "KA09IJ4567",
    "UP16KL2345",
    "MH22MN6789",
    "DL10OP1234",
    "KA11QR9876",
    "UP18ST5432",
    "MH24UV1111",
    "DL13WX2222",
    "KA15YZ3333",
    "UP20AA4444",
    "MH26BB5555",
    "KA17CC6666",
    "UP22DD7777",
    "XX123456"      # Invalid Registration
]

# Dictionary to count vehicles state-wise
state_report = {}

# List to store invalid registrations
invalid_registrations = []

# ==========================================
# Analyze Each Vehicle Number
# ==========================================

for vehicle in vehicles:

    print("\n================================")
    print("Vehicle Number :", vehicle)
    print("================================")

    # --------------------------------------
    # Extract different parts
    # --------------------------------------

    state_code = vehicle[0:2]

    district_code = vehicle[2:4]

    series = vehicle[4:6]

    vehicle_number = vehicle[6:]

    # --------------------------------------
    # Count letters and digits
    # --------------------------------------

    letters = 0
    digits = 0

    for ch in vehicle:

        if ch.isalpha():
            letters += 1

        elif ch.isdigit():
            digits += 1

    # --------------------------------------
    # Validate Registration Format
    #
    # Format:
    # First 2 = Alphabets
    # Next 2 = Digits
    # Next 2 = Alphabets
    # Last 4 = Digits
    # Total Length = 10
    # --------------------------------------

    valid = True

    if len(vehicle) != 10:
        valid = False

    elif not vehicle[0:2].isalpha():
        valid = False

    elif not vehicle[2:4].isdigit():
        valid = False

    elif not vehicle[4:6].isalpha():
        valid = False

    elif not vehicle[6:10].isdigit():
        valid = False

    # --------------------------------------
    # If Valid Registration
    # --------------------------------------

    if valid:

        print("State Code    :", state_code)
        print("District Code :", district_code)
        print("Series        :", series)
        print("Vehicle No.   :", vehicle_number)

        print("Letters Count :", letters)
        print("Digits Count  :", digits)

        print("Status        : Valid")

        # ----------------------------------
        # Count vehicles state-wise
        # ----------------------------------

        if state_code in state_report:
            state_report[state_code] += 1
        else:
            state_report[state_code] = 1

    # --------------------------------------
    # If Invalid Registration
    # --------------------------------------

    else:

        print("Status : Invalid Registration")

        invalid_registrations.append(vehicle)

# ==========================================
# Display Invalid Registrations
# ==========================================

print("\n\n================================")
print("INVALID REGISTRATIONS")
print("================================")

if len(invalid_registrations) > 0:

    for vehicle in invalid_registrations:
        print(vehicle)

else:
    print("No Invalid Registrations Found")

# ==========================================
# State Wise Report
# ==========================================

print("\n\n================================")
print("STATE WISE REPORT")
print("================================")

for state in state_report:

    print(state, "->", state_report[state], "Vehicles")

# ==========================================
# Final Summary
# ==========================================

print("\n================================")
print("FINAL REPORT")
print("================================")

print("Total Vehicles Checked :", len(vehicles))

print("Valid Vehicles         :",
    len(vehicles) - len(invalid_registrations))

print("Invalid Vehicles       :",
    len(invalid_registrations))