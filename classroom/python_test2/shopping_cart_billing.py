"""Problem 14: Shopping Cart Billing System 
Problem Statement 
The prices of products purchased by a customer are stored in a tuple. 
Sample Data 
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200) 
Tasks 
1. Calculate the total bill amount.  
2. Find the most expensive product.  
3. Find the least expensive product.  
4. Count products costing more than ₹1,000.  
5. Create a list of products eligible for discount (price > ₹800).  
Sample Output 
Total Bill Amount: ₹8,248 
 
Most Expensive Product: ₹1,500 
 
Least Expensive Product: ₹250 
Products Costing More Than ₹1,000: 3 
Discount Eligible Products: 
[1250, 999, 1500, 850, 1200]"""
#======================================
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200)

#======================================
# 1. Calculate the total bill amount.
#======================================
total = 0
for price in prices:
    total += price
print("Total Bill Amount:", total)
#======================================
# 2. Find the most expensive product.
#======================================
highest = 0
for price in prices:
    if price > highest:
        highest = price
print("\nMost Expensive Product:", highest)

#======================================
# 3. Find the least expensive product
#======================================
lowest = float('inf')
for price in prices:
    if price < lowest:
        lowest = price
        lowest_product = price
print("\nLeast Expensive Product:", lowest)
#======================================
# 4. Count products costing more than ₹1,000.
#======================================
count = 0
for price in prices:
    if price > 1000:
        count += 1
print("\nProducts Costing More Than ₹1,000:", count)
#======================================
# 5. Create a list of products eligible for discount (price > ₹800).
#======================================
print("\nDiscount Eligible Products:")
for price in prices:
    if price > 800:
        print(price)
#======================================
