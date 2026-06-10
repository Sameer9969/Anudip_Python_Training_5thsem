"""2. Write a program to copy entire content from one file into another"""





# Open source file in read mode
file1 = open("source.txt", "r")

# Read all content
data = file1.read()

# Close source file
file1.close()

# Open destination file in write mode
file2 = open("destination.txt", "w")

# Write content into destination file
file2.write(data)

# Close destination file
file2.close()

print("Content copied successfully!")
#================================================