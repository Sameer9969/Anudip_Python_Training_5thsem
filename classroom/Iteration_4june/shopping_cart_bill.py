#A customer is adding items to a shopping cart. The price of each item is entered one by one. 
#Write a program that continuously accepts item prices and calculates the total bill amount. The program should stop accepting 
#prices when the user enters 0.
# --------------------------------
total_bill = 0
while(True):
    price = int(input("enter the price of iteam : "))
    if(price < 0):
        print("invalid price try again")
    elif(price == 0):
        break
    total_bill += price 
print("total bill amount:", total_bill)
print("--------------------------------")
