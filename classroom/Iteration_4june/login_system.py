#A website allows users to log in using a password. The correct password is admin123. 
#Write a program that keeps asking the user to enter the password until the correct password is provided.
#--------------------------------
correct_password = "admin123"
while(True):
    user_password = input("enter the password :")
    if(user_password == correct_password):
        print("correct password account accessed")
        break
    else:
        print("incorrect password try again")