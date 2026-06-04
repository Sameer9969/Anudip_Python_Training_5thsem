#A game has selected a secret number 7. The player must keep guessing the number until the correct guess is made. 
#Write a program that repeatedly asks the user to guess the number and displays a success message when the correct number is 
#entered. 
guess_number = 7
while(True):
    user_guess = int(input("guess the number :"))
    if(user_guess == guess_number):
        print("congratulations you guessed correct the number")
        break
    else:
        print("Wrong Guess. Try Again. ")