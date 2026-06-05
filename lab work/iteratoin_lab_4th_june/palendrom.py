# Problem Statement: 
# Accept a number from the user. 
# Display: 
# • Reverse Number  
# • Whether it is a Palindrome  
# Take input from user
num = int(input("Enter a number: "))

# Store original number (because num will change in loop)
original = num

# Variable to store reverse number
reverse = 0

# Loop runs until number becomes 0
while num > 0:

    # Get last digit of number
    digit = num % 10

    # Build reverse number step by step
    reverse = reverse * 10 + digit

    # Remove last digit from number
    num = num // 10

# Print reversed number
print("Reverse Number =", reverse)

# Check palindrome condition
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome")