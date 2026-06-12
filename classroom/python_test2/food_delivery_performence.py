"""Problem 3: Food Delivery Performance Dashboard 
Problem Statement 
Delivery times (in minutes) for different orders are recorded below: 
Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 
1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.  
4. Display delayed orders (>45 minutes).  
5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes)  
Sample Output 
Fastest Delivery: 18 minutes 
 
Slowest Delivery: 80 minutes 
 
Average Delivery Time: 40.8 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Fast Deliveries: 4 
Normal Deliveries: 3 
Delayed Deliveries: 3"""




delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Fastest delivery
fastest = min(delivery_times)
print("Fastest Delivery:", fastest, "minutes")

# Slowest delivery
slowest = max(delivery_times)
print("Slowest Delivery:", slowest, "minutes")

# Average delivery time
average = sum(delivery_times) / len(delivery_times)
print("Average Delivery Time:", average, "minutes")

# Delayed orders
delayed_orders = []

for time in delivery_times:
    if time > 45:
        delayed_orders.append(time)

print("Delayed Orders:")
print(delayed_orders)

# Categorize deliveries
fast_count = 0
normal_count = 0
delayed_count = 0

for time in delivery_times:
    if time <= 30:
        fast_count += 1
    elif time <= 45:
        normal_count += 1
    else:
        delayed_count += 1

print("Fast Deliveries:", fast_count)
print("Normal Deliveries:", normal_count)
print("Delayed Deliveries:", delayed_count)