#Accept a number from the user and determine whether it is a prime number or not. 
#Additional Requirement: 
#If the number is not prime, display all its factors.

num = int(input("enter the number :"))
i = 1
count = 0
print("Factors are: ", end="")

while i <= num:
    if num % i == 0:
        print(i, end=" ")
        count += 1
    i += 1

print()

if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
print("------------------------------")