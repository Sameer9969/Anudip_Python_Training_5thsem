"""wap to input the string or sentence from user and count the number of characters present in it withput useing len  function"""
user_sentence = input("enter the sentence : ")
count = 0
for i in user_sentence:
    count += 1
print(count)