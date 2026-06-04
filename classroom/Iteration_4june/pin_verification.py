#An ATM machine requires the user to enter the correct PIN to access their account. The valid PIN is 1234. 
#Write a program that repeatedly asks the user to enter a PIN until the correct PIN is entered. 
#--------------------------------
correct_pin = 1234
while(True):
    user_pin = int(input("enter the pin :"))
    if(user_pin == correct_pin):
        print("correct pin account accessed")
        break
    else:
        print("incorrect pin try again")