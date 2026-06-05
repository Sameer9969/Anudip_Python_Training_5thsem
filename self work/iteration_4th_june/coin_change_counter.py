# Problem Statement: 
# Given an amount, determine the minimum number of notes required using: 
# ₹500, ₹200, ₹100, ₹50, ₹20, ₹10
#enter the number for exchange
amount = int(input("enter the amount : "))
amount500 = amount // 500
amount = amount % 500

amount200 = amount // 200
amount = amount % 200

amount100 = amount // 100
amount = amount % 100

amount50 = amount // 50
amount = amount % 50

amount20 = amount // 20
amount = amount % 20

amount10 = amount // 10
amount = amount % 10

print("500 notes =", amount500)
print("200 notes =", amount200)
print("100 notes =", amount100)
print("50 notes =", amount50)
print("20 notes =", amount20)
print("10 notes =", amount10)
print("Remaining amount =", amount)