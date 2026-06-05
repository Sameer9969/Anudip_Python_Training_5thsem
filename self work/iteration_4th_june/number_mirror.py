# Check whether the left half of a number is identical to the right half. 
# Example: 
# Input: 123123 
# Output: Mirror Number 
# Input: 123456 
# Output: Not a Mirror Number
#enter the  number
num = input("Enter a number: ")
#for lenght of digite
n = len(num)
#check for mirror

if n % 2 != 0:
    print("Not a Mirror Number")
else:
    half = n // 2

    left = num[:half]
    right = num[half:]

    if left == right:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")