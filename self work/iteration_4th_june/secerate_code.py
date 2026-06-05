# Problem Statement: 
# A secret code is valid if: 
# • It contains exactly 6 digits.  
# • Sum of first 3 digits equals sum of last 3 digits.  
# Example: 
# Input: 123321 
# Output: Valid Code 
# Input: 123456 
# Output: Invalid Code

# Accept a secret code from the user
num = int(input("Enter the number: "))

# Convert number to string and find its length
temp = len(str(num))

# Variables to store sum of first 3 digits and last 3 digits
sum1 = 0
sum2 = 0

# Check if the code contains exactly 6 digits
if temp != 6:
    print("Invalid Code")

else:
    # Convert number into string for indexing
    num = str(num)

    # Calculate sum of first 3 digits
    for i in range(3):
        sum1 += int(num[i])

    # Calculate sum of last 3 digits
    for i in range(3, 6):
        sum2 += int(num[i])

    # Display sums (for debugging/understanding)
    print("Sum of first 3 digits =", sum1)
    print("Sum of last 3 digits =", sum2)

    # Check whether both sums are equal
    if sum1 == sum2:
        print("Valid Code")
    else:
        print("Invalid Code")