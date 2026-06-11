"""Problem 5: Online Shopping Cart Analyzer 
Problem Statement 
The prices of products added to a shopping cart are stored below. 
Sample Data 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price.  
Sample Output 
Total Cart Value: ₹11,097 
 
Most Expensive Product: ₹2,500 
 
Cheapest Product: ₹300 
 
Premium Shipping Eligible Products: 4 
 
Discount Eligible Products: 
[2500, 1800] 
 
Average Product Price: ₹1,109.7"""
# Online Shopping Cart Analyzer

cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# 1. Total Cart Value
total = 0
for price in cart:
    total = total + price

print("Total Cart Value: ₹", total)

# 2. Most Expensive and Cheapest Product
most_expensive = cart[0]
cheapest = cart[0]

for price in cart:
    if price > most_expensive:
        most_expensive = price

    if price < cheapest:
        cheapest = price

print("\nMost Expensive Product: ₹", most_expensive)
print("Cheapest Product: ₹", cheapest)

# 3. Premium Shipping Eligible Products (price > 1000)
premium_count = 0

for price in cart:
    if price > 1000:
        premium_count += 1

print("\nPremium Shipping Eligible Products:", premium_count)

# 4. Discount Eligible Products (price > 1500)
discount_list = []

for price in cart:
    if price > 1500:
        discount_list.append(price)

print("\nDiscount Eligible Products:")
print(discount_list)

# 5. Average Product Price
average = total / len(cart)

print("\nAverage Product Price: ₹", average)