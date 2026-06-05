# Problem Statement 
# An inventory manager stores stock quantities as: 
# stock = [25, 5, 0, 12, 3, 18, 0, 30] 
# Write a program to: 
# 1. Display products that are out of stock.  
# 2. Display products that need restocking (quantity less than 10).  
# 3. Count available products.  
# 4. Create a new list containing only products with stock greater than or equal to 15. 
#-------------------------------------
stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = []
restocking = []
available_count = 0
good_stock = []

for qty in stock:

    # 1. Out of stock
    if qty == 0:
        out_of_stock.append(qty)

    # 2. Need restocking
    elif qty < 10:
        restocking.append(qty)

    # 3. Available products
    if qty > 0:
        available_count += 1

    # 4. Stock >= 15
    if qty >= 15:
        good_stock.append(qty)

print("Out of Stock Products :", out_of_stock)
print("Need Restocking :", restocking)
print("Available Products :", available_count)
print("Stock >= 15 :", good_stock)