# Problem Statement: 
# Accept a number and check whether every digit is exactly 1 greater than its previous digit. 
# Example: 
# Input: 12345 
# Output: Consecutive Number 
# Input: 1357 
# Output: Not a Consecutive Number
#------------------------------------
num = int(input("Enter a number: "))

prev = num % 10 #last digite leta hai 
num //= 10 #last digite ko remove karta hai total digite

flag = True

while num > 0:
    curr = num % 10 #bache hue number ko modules ki help se rest of number ki last digite ko curr me store karo

    if prev - curr != 1:#previous - curr
        flag = False
        break
    prev = curr
    num //= 10

if flag:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")