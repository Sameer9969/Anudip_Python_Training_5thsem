"""2. Inventory Management System 
Sample Data 
inventory = { 
    "Notebook": 45, 
    "Pen": 120, 
    "Pencil": 80, 
    "Eraser": 25, 
    "Marker": 15, 
    "Stapler": 8, 
    "Glue": 12, 
    "Scale": 30, 
    "Folder": 5, 
    "Calculator": 3 
} 
Tasks 
• Display products with stock less than 10.  
• Count products having stock more than 50.  
• Find the product with the minimum stock.  
• Create a list of products that require restocking (stock < 20).  
• Calculate the total inventory count. """

# Inventory dictionary jisme product name key hai aur stock value hai
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# -----------------------------------
# 1. Display products with stock less than 10
# -----------------------------------

print("Products with stock less than 10:")

# Dictionary ke har key-value pair par loop chalega
for product, stock in inventory.items():

    # Check karo stock 10 se kam hai ya nahi
    if stock < 10:

        # Product ka naam print karo
        print(product)

# -----------------------------------
# 2. Count products having stock more than 50
# -----------------------------------

# Count store karne ke liye variable
count = 0

# Sirf values (stock) par loop chalao
for stock in inventory.values():

    # Check karo stock 50 se zyada hai ya nahi
    if stock > 50:

        # Count ko 1 se increase karo
        count += 1

# Final count print karo
print("Products having stock more than 50:", count)

# -----------------------------------
# 3. Find the product with minimum stock
# -----------------------------------

# Product name store karne ke liye variable
min_product = ""

# Minimum stock ko bahut bade number se initialize kiya
min_stock = float('inf')

# Dictionary ke har key-value pair par loop
for product, stock in inventory.items():

    # Agar current stock minimum stock se kam hai
    if stock < min_stock:

        # Minimum stock update karo
        min_stock = stock

        # Product name update karo
        min_product = product

# Minimum stock wala product print karo
print("Product with minimum stock:", min_product)

# Uska stock bhi print karo
print("Stock:", min_stock)

# -----------------------------------
# 4. Create a list of products requiring restocking
# -----------------------------------

# Empty list create karo
restock_list = []

# Dictionary ke har item par loop
for product, stock in inventory.items():

    # Check karo stock 20 se kam hai ya nahi
    if stock < 20:

        # Product ko list me add karo
        restock_list.append(product)

# Restocking products ki list print karo
print("Products requiring restocking:", restock_list)

# -----------------------------------
# 5. Calculate total inventory count
# -----------------------------------

# Total stock store karne ke liye variable
total_inventory = 0

# Sabhi stock values par loop
for stock in inventory.values():

    # Har stock ko total me add karo
    total_inventory += stock

# Total inventory print karo
print("Total Inventory Count:", total_inventory)