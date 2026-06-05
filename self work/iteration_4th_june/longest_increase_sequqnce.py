# Problem Statement: 
# Accept N numbers one by one and find the length of the longest continuous increasing sequence. 
# Example: 
# Input: 
# 5 8 10 12 3 4 5 6 1 
 
# Output: 
# Longest Sequence Length = 4
n = int(input("Enter number of elements: "))

prev = int(input("Enter number: "))

current_len = 1
max_len = 1

for i in range(1, n):
    num = int(input("Enter number: "))

    if num > prev:
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 1

    prev = num

if current_len > max_len:
    max_len = current_len

print("Longest Sequence Length =", max_len)
