# Problem Statement 
# Given a list: 
# numbers = [4, 5, 6, 10, 11, 15, 16, 17] 
# Write a program to find all pairs of consecutive numbers. 
# Expected Output 
# 4 and 5 are consecutive 
# 5 and 6 are consecutive 
# 10 and 11 are consecutive 
# 15 and 16 are consecutive 
# 16 and 17 are consecutive
number = [4, 5, 6, 10, 11, 15, 16, 17]

for i in range(len(number) - 1):
    if number[i + 1] - number[i] == 1:
        print(number[i], "and", number[i + 1], "are consecutive")