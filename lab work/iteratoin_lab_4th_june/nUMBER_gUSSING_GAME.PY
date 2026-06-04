# Problem Statement: 
# Generate a secret number between 1 and 50. 
# Allow the user to keep guessing until the correct number is found. 
# Display: 
# • "Too High"  
# • "Too Low"  
# • "Correct Guess"  
# Also display the total number of attempts
guss_num = 32
num = int(input("enter the number between 1 to 50 : "))
while(num <= 50):
    if(num == guss_num):
        print("Correct Guess")
        break
    elif(num > guss_num):
        print("Too High")
    else:
        print("Too Low")
    num = int(input("enter the number between 1 to 50 : "))
print("------------------------------" )