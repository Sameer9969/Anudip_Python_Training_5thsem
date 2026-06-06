'''1. E-Commerce Order Analysis 
Problem Statement 
An online store records orders as: 
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. 
'''
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
]

# • Display all products costing more than ₹1000
print("Products Costing More Than ₹1000:")
for order in orders:
    if order[1] > 1000:
        print(order[0])

# • Find the most expensive product
most_expensive = orders[0]
for order in orders:
    if order[1] > most_expensive[1]:
        most_expensive = order

print("\nMost Expensive Product:")
print(most_expensive[0])

# • Calculate the total order value
total_value = 0
for order in orders:
    total_value += order[1]

print("\nTotal Order Value:", total_value)

# Count products costing below ₹1000.
count  = 0
for order in orders:
    if (order[1] < 1000):
        count += 1
        
print("\nProducts Costing Below ₹1000:", count)

