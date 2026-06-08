"""Problem Statement 
An e-commerce company stores product sales data as: 
sales = { 
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
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30.  
Sample Output 
Products Sold More Than 20 Times: 
Mouse 
Keyboard 
Headphones 
Router 

Best Selling Product: Mouse (45) 

Least Selling Product: Printer (8) 

Total Units Sold: 213 

Products Requiring Promotion: 
['Monitor', 'Printer', 'Tablet'] 

Products Having Sales Between 10 and 30: 6 
"""

sales = { 
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
#=============================================
# 1. Display products sold more than 20 times.
#=============================================
print("Products Sold More Than 20 Times:")
for product, quantity in sales.items():
    if quantity > 20:
        print(product)
#=============================================
# 2. Find the best-selling product
#=============================================
best_selling = 0
best_product = ""
for product, quantity in sales.items():
    if quantity > best_selling:
        best_selling = quantity
        best_product = product
print("\nBest Selling Product:", best_product, "(", best_selling, ")")

#=============================================
# 3. Find the least-selling product. 
#=============================================
least_selling = float('inf')
least_product = ""

for product, quantity in sales.items():
    if quantity < least_selling:
        least_selling = quantity
        least_product = product

print("Least Selling Product:", least_product, "(", least_selling, ")")


#=============================================
#  4. Calculate total products sold.
#=============================================
total_units_sold = 0
for quantity in sales.values():
    total_units_sold += quantity

print("\nTotal Units Sold:", total_units_sold)

#=============================================
# 5.Create a list of products requiring promotion (sales < 15).  
#=============================================
product = 0
promotion_products = []
for product, quantity in sales.items():
    if quantity < 15:
        promotion_products.append(product)

print("\nProducts Requiring Promotion:", promotion_products)

#=============================================  
#6. Count products having sales between 10 and 30.  
#Sample Output 
#Products Sold More Than 20 Times: 
#Mouse 
#Keyboard 
#Headphones 
#Router 
#===============================================
count = 0
for quantity in sales.values():
    if (10 < quantity < 30):
        count += 1

print("\nProducts Having Sales Between 10 and 30:", count)

