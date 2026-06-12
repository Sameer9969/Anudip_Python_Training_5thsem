"""Problem Statement 
Daily sales figures (in ₹) for 10 days are stored in a list. 
Sample Data 
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000] 
Tasks 
1. Find the highest sales.  
2. Find the lowest sales.  
3. Calculate average sales.  
4. Count days with sales above ₹20,000.  
5. Display sales figures below average.  
Sample Output 
Highest Sales: ₹30,000 
 
Lowest Sales: ₹15,000 
 
Average Sales: ₹22,100 
 
Days with Sales Above ₹20,000: 5 
 
Sales Below Average: 
[15000, 18000, 17000, 21000, 19000]"""


sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]

# 1. Highest Sales
highest = max(sales)
print("Highest Sales: ₹", highest)

# 2. Lowest Sales
lowest = min(sales)
print("Lowest Sales: ₹", lowest)

# 3. Average Sales
total = sum(sales)
average = total / len(sales)
print("Average Sales: ₹", average)

# 4. Days with Sales Above ₹20,000
count = 0
for sale in sales:
    if sale > 20000:
        count += 1

print("Days with Sales Above ₹20,000:", count)

# 5. Sales Below Average
below_average = []

for sale in sales:
    if sale < average:
        below_average.append(sale)

print("Sales Below Average:")
print(below_average)