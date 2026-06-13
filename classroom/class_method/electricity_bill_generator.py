"""9. Electricity Bill Generator (Intermediate) 
Problem Statement: 
Create an ElectricityBill class containing: 
• Consumer Name  
• Consumer Number  
• Units Consumed  
Implement methods to: 
• Calculate electricity charges using the following slab:  
Units Rate 
First 100 units ₹5/unit 
Next 100 units ₹7/unit 
Above 200 units ₹10/unit 
• Display the final bill.  
Sample Output: 
Consumer Name : Amit 
Units Consumed: 250 
Total Bill    : ₹1700"""

class ElectricityBill:
    def __init__(self, name, consumer_no, units):
        self.name = name
        self.consumer_no = consumer_no
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5

        elif self.units <= 200:
            bill = (100 * 5) + ((self.units - 100) * 7)

        else:
            bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

        return bill

    def display_bill(self):
        total_bill = self.calculate_bill()

        print("\n----- ELECTRICITY BILL -----")
        print("Consumer Name  :", self.name)
        print("Consumer No.   :", self.consumer_no)
        print("Units Consumed :", self.units)
        print("Total Bill     : ₹", total_bill)


# Input
name = input("Enter Consumer Name: ")
consumer_no = input("Enter Consumer Number: ")
units = int(input("Enter Units Consumed: "))

# Object Creation
bill = ElectricityBill(name, consumer_no, units)

# Display Bill
bill.display_bill()