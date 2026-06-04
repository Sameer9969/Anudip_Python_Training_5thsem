# Problem Statement: 
# Initial Balance = ₹10,000 
# Display a menu repeatedly: 
# 1. Check Balance 
# 2. Deposit 
# 3. Withdraw 
# 4. Exit 
# Requirements: 
# • Withdrawal should not exceed balance.  
# • Display appropriate messages.  
# • Continue until Exit is selected. 
print("-------- ATM MACHINE --------")

balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Check Balance
    if choice == 1:
        print("Your current balance is:", balance)

    # Deposit
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))

        if amount > 0:
            balance += amount
            print("Amount deposited successfully.")
            print("Current balance is:", balance)
        else:
            print("Invalid amount. Please enter a positive value.")

    # Withdraw
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount.")

        elif amount < 500:
            print("Minimum withdrawal amount is 500.")

        elif amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully.")
            print("Current balance is:", balance)

        else:
            print("Insufficient balance.")

    # Exit
    elif choice == 4:
        print("Program exited.")
        print("Thank you for using our ATM.")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")

print("------------------------------")

    


    

