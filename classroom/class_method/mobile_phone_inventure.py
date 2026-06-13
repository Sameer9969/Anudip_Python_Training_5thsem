"""8. Mobile Phone Inventory (Intermediate) 
Problem Statement: 
Create a MobilePhone class to store: 
• Brand Name  
• Model Name  
• Price  
• Available Stock  
Implement methods to: 
• Display phone details.  
• Sell a specified quantity of phones.  
• Update stock after sale.  
Display an appropriate message if sufficient stock is unavailable. 
Sample Output: 
Sale Successful. 
Remaining Stock: 12"""

class MobilePhone:
    def __init__(self, brand, model, price, stock):
        self.brand = brand
        self.model = model
        self.price = price
        self.stock = stock

    def display_details(self):
        print("\nBrand :", self.brand)
        print("Model :", self.model)
        print("Price : ₹", self.price)
        print("Stock :", self.stock)

    def sell_phone(self, quantity):
        if quantity <= self.stock:
            self.stock = self.stock - quantity
            print("\nSale Successful.")
            print("Remaining Stock:", self.stock)
        else:
            print("\nInsufficient Stock Available.")


# Input
brand = input("Enter Brand Name: ")
model = input("Enter Model Name: ")
price = int(input("Enter Price: "))
stock = int(input("Enter Available Stock: "))

# Object Creation
phone = MobilePhone(brand, model, price, stock)

# Display Details
phone.display_details()

# Sell Phones
quantity = int(input("\nEnter Quantity to Sell: "))
phone.sell_phone(quantity)