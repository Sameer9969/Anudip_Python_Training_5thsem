# Problem Statement: 
# A Mountain Number is a number whose digits first increase and then decrease. 
# Example: 
# Input: 12321 
# Output: Mountain Number 

# Input: 12345 
# Output: Not a Mountain Number

num = input("Enter a number: ")

increasing = False
decreasing = False

# Check adjacent digits
for i in range(len(num) - 1):

    # Increasing part
    if num[i] < num[i + 1]:

        # Agar decrease ke baad increase mila
        if decreasing:
            print("Not a Mountain Number")
            break

        increasing = True

    # Decreasing part
    elif num[i] > num[i + 1]:

        # Mountain me pehle increase hona chahiye
        if not increasing:
            print("Not a Mountain Number")
            break

        decreasing = True

    # Equal digits allowed nahi hain
    else:
        print("Not a Mountain Number")
        break

else:
    # Loop successfully complete hua
    if increasing and decreasing:
        print("Mountain Number")
    else:
        print("Not a Mountain Number")