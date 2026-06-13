"""7. Vehicle Rental System (Intermediate)
Problem Statement:
Design a Vehicle class containing:
• Vehicle Number
• Vehicle Type
• Rent per Day
Implement methods to:
• Accept vehicle details.
• Calculate total rental amount based on the number of days rented.
• Display the bill.
Sample Output:
Vehicle Type : Car
Days Rented  : 5
Total Rent   : ₹10000
"""

class Vehicle:
    def __init__(self, vehicle_number, vehicle_type, rent_per_day):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.rent_per_day = rent_per_day

    def calculate_rent(self, days):
        return self.rent_per_day * days

    def display_bill(self, days):
        total_rent = self.calculate_rent(days)

        print("\nVehicle Number :", self.vehicle_number)
        print("Vehicle Type   :", self.vehicle_type)
        print("Days Rented    :", days)
        print("Total Rent     : ₹", total_rent)


# Input
vehicle_number = input("Enter Vehicle Number: ")
vehicle_type = input("Enter Vehicle Type: ")
rent_per_day = int(input("Enter Rent per Day: "))
days = int(input("Enter Number of Days Rented: "))

# Object Creation
v1 = Vehicle(vehicle_number, vehicle_type, rent_per_day)

# Display Bill
v1.display_bill(days)
