"""4. Vehicle Number Plate Verification 
Problem Statement 
A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid.  
Sample Output 
Vehicle Number: MH12AB4589 
State Code: MH 
District Code: 12 
Series: AB 
Vehicle Number: 4589 
 
Total Letters: 4 
Total Digits: 6 
 
Vehicle Number Status: Valid"""



#----------------------------------------------
# Vehicle Number Plate Verification
#----------------------------------------------

vehicle_no = "MH12AB4589"

print("Vehicle Number:", vehicle_no)

#----------------------------------------------
# 1. Extract state code
#----------------------------------------------
state_code = vehicle_no[0:2]
print("State Code:", state_code)

#----------------------------------------------
# 2. Extract district code
#----------------------------------------------
district_code = vehicle_no[2:4]
print("District Code:", district_code)

#----------------------------------------------
# 3. Extract vehicle series
#----------------------------------------------
series = vehicle_no[4:6]
print("Series:", series)

#----------------------------------------------
# 4. Extract vehicle number
#----------------------------------------------
number = vehicle_no[6:10]
print("Vehicle Number:", number)

#----------------------------------------------
# 5. Count letters and digits
#----------------------------------------------
letters = 0
digits = 0

for char in vehicle_no:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("\nTotal Letters:", letters)
print("Total Digits:", digits)

#----------------------------------------------
# 6 & 7. Verify and Display Status
#----------------------------------------------

if (vehicle_no[0:2].isalpha() and
    vehicle_no[2:4].isdigit() and
    vehicle_no[4:6].isalpha() and
    vehicle_no[6:10].isdigit() and
    len(vehicle_no) == 10):

    print("\nVehicle Number Status: Valid")

else:
    print("\nVehicle Number Status: Invalid")
#----------------------------------------------