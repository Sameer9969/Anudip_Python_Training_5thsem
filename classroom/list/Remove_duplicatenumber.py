# wap to create a list of 20 number given by user. ask the user the input any other number.
# remove all the duplicate of this number from the list.

#------------------------------------
num = []
#taking input
for i in range(1, 21):
    number = int(input("enter the  number"))
    num.append(number)

# the number that have to remove and reverse the list

n = int(input("enter the number thet have to remove"))
for i in range(len(num)-1):
    if num[i] == n:
        num.pop(i)
print(num)
#------------------------------------

