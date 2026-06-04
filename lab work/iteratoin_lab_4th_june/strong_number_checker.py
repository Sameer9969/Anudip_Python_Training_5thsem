#Problem Statement: 
#A Strong Number is a number whose sum of factorials of digits equals the number itself. 
#Write a program to check whether a given number is a Strong Number.

#------------------------------


num = int(input("Enter a number: "))

temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i += 1

    sum_fact += fact
    temp = temp // 10

if sum_fact == num:
    print("Strong Number")
else:
    print("Not a Strong Number")