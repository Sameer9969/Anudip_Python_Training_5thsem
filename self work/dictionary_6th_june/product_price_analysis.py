"""prices = { 
    "Laptop": 55000, 
    "Mouse": 800, 
    "Keyboard": 1800, 
    "Monitor": 12000, 
    "Printer": 9000, 
    "Tablet": 28000, 
    "Speaker": 3500, 
    "Webcam": 2500, 
    "Headphones": 4200, 
    "Router": 3200 
} 
Tasks 
• Display products costing more than ₹5000.  
• Count products costing less than ₹3000.  
• Find the most expensive product.  
• Create a list of products priced between ₹2000 and ₹10000.  
• Calculate the total value of all products. """
# Product prices dictionary
# Key = Product Name
# Value = Price of Product

prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# ==================================================
# 1. Display products costing more than ₹5000
# ==================================================

print("Products costing more than ₹5000:")

# Loop through each product and price
for product, price in prices.items():

    # Check if price is greater than 5000
    if price > 5000:

        # Print product name
        print(product)

# ==================================================
# 2. Count products costing less than ₹3000
# ==================================================

# Variable to store count
count = 0

# Loop through all prices
for price in prices.values():

    # Check if price is less than 3000
    if price < 3000:

        # Increase count by 1
        count += 1

# Display total count
print("Products costing less than ₹3000:", count)

# ==================================================
# 3. Find the most expensive product
# ==================================================

# Variable to store product name
most_expensive_product = ""

# Variable to store highest price
highest_price = 0

# Loop through each product and price
for product, price in prices.items():

    # Check if current price is greater than highest price
    if price > highest_price:

        # Update highest price
        highest_price = price

        # Store product name
        most_expensive_product = product

# Display most expensive product
print("Most Expensive Product:", most_expensive_product)

# Display its price
print("Price:", highest_price)

# ==================================================
# 4. Create a list of products priced between
#    ₹2000 and ₹10000
# ==================================================

# Empty list to store product names
product_list = []

# Loop through each product and price
for product, price in prices.items():

    # Check if price lies between 2000 and 10000
    if price >= 2000 and price <= 10000:

        # Add product name to list
        product_list.append(product)

# Display list
print("Products priced between ₹2000 and ₹10000:")
print(product_list)

# ==================================================
# 5. Calculate the total value of all products
# ==================================================

# Variable to store total value
total_value = 0

# Loop through all prices
for price in prices.values():

    # Add current price to total value
    total_value += price

# Display total value
print("Total Value of All Products:", total_value)