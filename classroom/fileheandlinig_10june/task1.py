"""Classwork : To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file."""

# to write in file
filev = open('demo.txt', 'w')
#to write the content in file
filev.write("hello i am sameer singh student of b tech" \
"hello i am sameer singh student of b tech" \
"hello i am sameer singh student of b tech" \
"v" \
"hello i am sameer singh student of b techhello i am sameer singh student of b tech")

#==========================================
#1. No. of Vowels in file.
#==========================================
vowel_count = 0
filev = open('demo.txt', 'r')
content = filev.read()
for char in content:
    if char in 'aeiouAEIOU':
        vowel_count += 1
print("Number of vowels in the file:", vowel_count)
#===========================================
#2. No. of characters into the file.
#===========================================
char_count = 0
filev = open('demo.txt', 'r')
content = filev.read()
for char in content:
    char_count += 1
print("Number of characters in the file:", char_count)

#==========================================
# 3. No. of lines into the file
#==========================================
line_count = 0
filev = open('demo.txt', 'r')
for line in filev:
    line_count += 1
print("Number of lines in the file:", line_count)

#file is closed
filev.close()
#==========================================
