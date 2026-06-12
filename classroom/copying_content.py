"""SAMEER SINGH 	

Question : Create a program to copy the contents o
f one file into another file and display the total number of lines copied."""
file1 = open("example.txt", "r")
file2 = open("demo1.txt", "w")

count = 0

for line in file1:
    file2.write(line)
    count += 1

file1.close()
file2.close()

print("Total lines copied:", count)
