# Problem Statement: 
# Calculate electricity bill based on the following slab rates: 
# Units Rate 
# 0-100 ₹5/unit 
# 101-200 ₹7/unit 
# Above 200 ₹10/unit 
# Display: 
# • Units Consumed  
# • Total Bill  
# • Category (Low / Medium / High Consumption)
#----------------------------
units = int(input("enter the units :"))
if(units <=100):
    bill = units *5
    print("Low Consumption : ",bill)
elif(units <= 200):
    bill = units *7
    print("Medium Consumption : ",bill)
else:
    bill = units *10
    print("High Consumption : ",bill)