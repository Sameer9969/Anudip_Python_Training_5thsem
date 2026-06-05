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
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] == 1:
        print(numbers[i], "and", numbers[i + 1], "are consecutive")