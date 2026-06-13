"""1. Student Information System (Basic) 
Problem Statement: 
Create a Student class to store the student's name, roll number, and marks obtained in three subjects. 
Implement methods to: 
• Accept student details.  
• Calculate the total marks.  
• Calculate the percentage.  
• Display the complete student report.  
Sample Output: 
Name       : Ananya 
Roll No    : 101 
Total Marks: 255 
Percentage : 85.0%"""
#student information system
class Student:
    def __init__(self, name, roll_no, sub1,sub2,sub3):
        self.name = name
        self.roll_no = roll_no
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    # Method to calculate total marks
    def calculate_total(self):
        total_marks = self.sub1 + self.sub2 + self.sub3
        return total_marks



    # Method to calculate percentage
    def calculate_percentage(self):
        total_marks = self.calculate_total()
        percentage = (total_marks / 300) * 100
        return percentage






    # Method to display student report
    def display_report(self):
        total_marks = self.calculate_total()
        percentage = self.calculate_percentage()
        print("Name       :", self.name)
        print("Roll No    :", self.roll_no)
        print("Total Marks:", total_marks)
        print("Percentage :", percentage, "%")
#---------------------------------------------------
#---------------main program -----------------------
#---------------------------------------------------
name = input("Enter the student's name: ")
roll_no = int(input("Enter the student's roll number: "))
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

# Create object of Student class
student = Student(name, roll_no, sub1, sub2, sub3)

# Call methods using the object
print("Student Report")
student.display_report()
#---------------------------------------------------
