# A customer's transactions are stored as: 
# transactions = [5000, -2000, 3000, -1000, -500, 7000] 
# Positive values represent deposits and negative values represent withdrawals. 
# Write a program to: 
# 1. Calculate the current balance.  
# 2. Count total deposits and withdrawals.  
# 3. Find the largest deposit and largest withdrawal.  
# 4. Create separate lists for deposits and withdrawals. 

 
transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0

deposits = []
withdrawals = []

deposit_count = 0
withdrawal_count = 0

for amount in transactions:
# current balence
    balance = balance +amount
# total amount deposits and withdrawals. 
    if amount > 0:
        deposits.append(amount)
        deposit_count += 1

    elif amount < 0:
        withdrawals.append(amount)
        withdrawal_count += 1

# Largest Deposit
largest_deposit = deposits[0]

for deposit in deposits:
    if deposit > largest_deposit:
        largest_deposit = deposit

# Largest Withdrawal
largest_withdrawal = withdrawals[0]

for withdrawal in withdrawals:
    if withdrawal < largest_withdrawal:
        largest_withdrawal = withdrawal

print("Current Balance =", balance)
print("Total Deposits =", deposit_count)
print("Total Withdrawals =", withdrawal_count)
print("Largest Deposit =", largest_deposit)
print("Largest Withdrawal =", largest_withdrawal)
print("Deposits List =", deposits)
print("Withdrawals List =", withdrawals)
