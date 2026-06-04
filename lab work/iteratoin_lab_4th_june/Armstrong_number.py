#Problem Statement: 
#Accept a number from the user and check whether it is an Armstrong Number.
num = int(input("enter the number :"))
sum = 0
power = len(str(num))
temp = num
while(temp >0):
    num1 = temp % 10
    sum = sum+num1 ** power
    temp = temp//10
if(num == sum):
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")
print("------------------------------")

