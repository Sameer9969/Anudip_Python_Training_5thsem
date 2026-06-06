"""Product IDs and quality status: 
products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 
Write a program to: 
• Display failed product IDs.  
• Count passed and failed products.  
• Calculate pass percentage.  
• Stop checking if 3 failures are found. """


products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 

# Display failed product IDs
print("Failed Product IDs:")
for product in products:
    if product[1] == "Fail":
        print(product[0])


# Count passed and failed products
count_pass = 0
count_fail = 0

for product in products:
    if product[1] == "Pass":
        count_pass += 1
    else:
        count_fail += 1

print("\nPassed Products:", count_pass)
print("Failed Products:", count_fail)   

# Calculate pass percentage
pass_percentage = (count_pass / len(products)) * 100

print("\nPass Percentage:", pass_percentage)

# Stop checking if 3 failures are found
count = 0

for product in products:
    if product[1] == "Fail":
        count += 1
        if count == 3:
            print("3 failures found")
            break
else:
    print("No failures found")