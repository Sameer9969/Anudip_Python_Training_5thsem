# Problem Statement: 
# Accept the number of rows and print the following pattern: 
# For Input: 
# 5 
# Output: 
# 1 
# 12 
# 123 
# 1234 
# 12345 
# Challenge: 
# Print the reverse pattern as well.

print("-------------------------")

rows = int(input("enter the number of rows :"))
for i in range(1,rows+1): #number of rows 
    for j in range(1,i+1): #for number
        print(j,end="")
    print()
print("-------------------------")
