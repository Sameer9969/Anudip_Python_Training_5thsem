"""Problem 4: Online Shopping Inventory System 
Problem Statement 
An online store maintains stock quantities of products. 
Sample Data 
inventory = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products with stock below 15 units.  
2. Find the product with maximum stock.  
3. Find the product with minimum stock.  
4. Calculate total stock available.  
5. Create a list of products requiring restocking (<10 units).  
Sample Output 
Products with Stock Below 15: 
Monitor 
Printer 
Tablet 
 
Highest Stock Product: 
Mouse (45 units) 
 
Lowest Stock Product: 
Printer (8 units) 
 
Total Stock Available: 213 
 
Products Requiring Restocking: 
['Printer']"""

inventory = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products with stock below 15
print("Products with Stock Below 15:")
for product, stock in inventory.items():
    if stock < 15:
        print(product)

# 2. Product with maximum stock
max_product = max(inventory, key=inventory.get)
print("\nHighest Stock Product:")
print(max_product, f"({inventory[max_product]} units)")

# 3. Product with minimum stock
min_product = min(inventory, key=inventory.get)
print("\nLowest Stock Product:")
print(min_product, f"({inventory[min_product]} units)")

# 4. Total stock available
total_stock = sum(inventory.values())
print("\nTotal Stock Available:", total_stock)

# 5. Products requiring restocking (<10 units)
restocking = []

for product, stock in inventory.items():
    if stock < 10:
        restocking.append(product)

print("\nProducts Requiring Restocking:")
print(restocking)
#==========================================