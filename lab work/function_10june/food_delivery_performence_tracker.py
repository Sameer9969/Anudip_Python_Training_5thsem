"""2. Food Delivery Performance Tracker 
Problem Statement 
Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements 
Create the following functions: 
1. fastest_delivery(times) 
Returns the shortest delivery time. 
2. delayed_orders(times) 
Returns a list of orders taking more than 45 minutes. 
3. average_delivery_time(times) 
Returns the average delivery time. 
4. delivery_category(times) 
Displays order categories: 
• Fast → ≤ 30 minutes  
• Normal → 31–45 minutes  
• Delayed → > 45 minutes  
Sample Output 
Fastest Delivery: 18 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Average Delivery Time: 
40.8 minutes 
 
Categories: 
28 -> Fast 
45 -> Normal 
60 -> Delayed"""

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 

#============================================
#  1. fastest_delivery(times)
#============================================
def fastest_delivery(times):
    min_time = times[0]
    for time in times:
        if time < min_time:
            min_time = time
        return min_time
    
#===========================================
# 2. delayed_orders(times) 
# Returns a list of orders taking more than 45 minutes.
#===========================================
def delayed_orders(times):
    delayed = []
    for time in times:
        if time > 45:
            delayed.append(time)
    return delayed
#===========================================
#3. average_delivery_time(times) 
# Returns the average delivery time.
#==========================================
def average_delivery_time(times):
    total_time = sum(times)
    average_time = total_time / len(times)
    return average_time
#==========================================
# 4. delivery_category(times) 
# Displays order categories: 
# • Fast → ≤ 30
#• Normal → 31–45 minutes  
#• Delayed → > 45 minutes  
#==========================================
def delivery_category(times):
    for time in times:
        if time <= 30:
            print(time,"-> Fast")
        elif time <= 45:
            print(time,"-> Normal")
        else:
            print(time,"-> Delayed")

#==========================================
# function call
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")
print("\nDelayed Orders:", delayed_orders(delivery_time))
print("\nAverage Delivery Time:", average_delivery_time(delivery_time), "minutes")
print("\nCategories:")
delivery_category(delivery_time)
#==========================================