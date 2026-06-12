"""Problem 16: File Copy Utility 
Problem Statement 
Sample Input/Data 
Source File (notes.txt) 
Python supports file handling. 
Functions improve code reusability. 
Dictionaries store data in key-value pairs. 
Tasks 
1. Read the contents of the source file.  
2. Copy the entire content to another file named backup.txt.  
3. Display a success message.  
4. Verify whether both files contain the same number of lines.  
Sample Output 
File copied successfully. 
 
Source File Lines: 3 
 
Backup File Lines: 3 
 
Verification Status: Successful"""


# Open source file and read content
source_file = open("notes.txt", "r")
content = source_file.read()
source_file.close()

# Create backup file and copy content
backup_file = open("backup.txt", "w")
backup_file.write(content)
backup_file.close()

print("File copied successfully.")

# Count lines in source file
source_file = open("notes.txt", "r")
source_lines = len(source_file.readlines())
source_file.close()

# Count lines in backup file
backup_file = open("backup.txt", "r")
backup_lines = len(backup_file.readlines())
backup_file.close()

print("\nSource File Lines:", source_lines)
print("Backup File Lines:", backup_lines)

# Verification
if source_lines == backup_lines:
    print("\nVerification Status: Successful")
else:
    print("\nVerification Status: Failed")