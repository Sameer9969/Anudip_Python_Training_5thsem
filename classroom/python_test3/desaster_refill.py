"""Problem 4: Disaster Relief Resource Allocation 
Problem Statement 
Relief materials available at different warehouses are stored as dictionaries. 
    "Warehouse2": ["Water", "Food", "Tents"], 
    "Warehouse3": ["Medicine", "Tents", "Clothes"], 
    "Warehouse4": ["Food", "Water", "Medicine"] 
} 
Tasks 
1. Display all unique relief items.  
2. Find warehouses containing medicines.  
3. Count how many warehouses stock each resource.  
4. Identify the most widely available resource.  
5. Display resources available in all warehouses.  
Sample Output 
Unique Resources: 
{'Food', 'Medicine', 'Blankets', 'Water', 'Tents', 'Clothes'} 

Warehouses with Medicines: 
Warehouse1 
Warehouse3 
Warehouse4 

Resource Availability: 
Food : 3 
Medicine : 3 
Blankets : 1 
Water : 2 
Tents : 2 
Clothes : 1 

Most Widely Available Resources: 
Food 
Medicine 

Resources Available in All Warehouses: 
None"""
###########################cd classroom\python_test3
############################ python cyber_security_login_audit.py


warehouses = {
    "Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"],
    "Warehouse3": ["Medicine", "Tents", "Clothes"],
    "Warehouse4": ["Food", "Water", "Medicine"]
}

# 1. Display all unique relief items
unique_resources = set()

for items in warehouses.values():
    for item in items:
        unique_resources.add(item)

print("Unique Resources:")
print(unique_resources)

# 2. Find warehouses containing medicines
print("\nWarehouses with Medicines:")
for warehouse in warehouses:
    if "Medicine" in warehouses[warehouse]:
        print(warehouse)

# 3. Count how many warehouses stock each resource
resource_count = {}

for items in warehouses.values():
    for item in items:
        if item in resource_count:
            resource_count[item] += 1
        else:
            resource_count[item] = 1

print("\nResource Availability:")
for item in resource_count:
    print(item, ":", resource_count[item])

# 4. Identify the most widely available resource
max_count = max(resource_count.values())

print("\nMost Widely Available Resources:")
for item in resource_count:
    if resource_count[item] == max_count:
        print(item)

# 5. Display resources available in all warehouses
common_resources = set(warehouses["Warehouse1"])

for warehouse in warehouses:
    common_resources = common_resources.intersection(set(warehouses[warehouse]))

print("\nResources Available in All Warehouses:")
if len(common_resources) == 0:
    print("None")
else:
    print(common_resources)