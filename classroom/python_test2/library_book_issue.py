"""Problem 13: Library Book Issue Tracker 
Problem Statement 
A library stores the number of times books were issued during a month. 
Sample Data 
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25] 
Tasks 
1. Find the maximum number of issues.  
2. Find the minimum number of issues.  
3. Calculate the average number of issues.  
4. Count books issued more than 15 times.  
5. Create a list of books issued fewer than 10 times.  
Sample Output 
Maximum Issues: 30 
 
Minimum Issues: 5 
 
Average Issues: 16.5 
 
Books Issued More Than 15 Times: 5 
 
Books Issued Fewer Than 10 Times: 
[8, 5] """

#============================================
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

#============================================
# 1. Find the maximum number of issues.  
#============================================
max = 0
for issue in book_issues:
    if issue > max:
        max = issue
print("Maximum Issues:", max)

#============================================
# 2. Find the minimum number of issues.
#============================================
min = float("inf")
for issue in book_issues:
    if issue < min:
        min = issue
print("Minimum Issues:", min)
#===========================================
# 3. Calculate the average number of issues.
#===========================================
total = 0
for issue in book_issues:
    total += issue
    average = total / len(book_issues)
print("Average Issues:", average)
#===========================================
# 4. Count books issued more than 15 times.
#===========================================
count = 0
for issue in book_issues:
    if issue > 15:
        count += 1
print("Books Issued More Than 15 Times:", count)
#===========================================
# 5. Create a list of books issued fewer than 10 times.
#===========================================
print("Books Issued Fewer Than 10 Times:")
for issue in book_issues:
    if issue < 10:
        print(issue)
#===========================================