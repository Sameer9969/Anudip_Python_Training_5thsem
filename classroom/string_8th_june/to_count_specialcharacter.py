"""wap to input the sentence from user and count the number of special character present in the sentence"""
count = 0
user_input = input("enter the character : i")
for i in user_input:
    if not i.isalnum():
        count += 1
print(count)