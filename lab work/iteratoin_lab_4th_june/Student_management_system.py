# Problem Statement: 
# Accept marks of 5 subjects. 
# Display: 
# • Total Marks  
# • Percentage  
# • Grade  
# Grade Criteria: 
# Percentage Grade 
# >=90 A+ 
# >=75 A 
# >=60 B 
# >=40 C 
# <40 Fail 
# Also display the number of subjects failed.
#--------------------------------------
print("enter hte nummber of all four subject")
sub1 = int(input("enter the marks of sub1 :"))
sub2 = int(input("enter the marks of sub2 :"))
sub3 = int(input("enter the marks of sub3 :"))
sub4 = int(input("enter the marks of sub4 :"))
sub5 = int(input("enter the marks of sub5 :"))
if(sub1 >0 and sub2 >0 and sub3 >0 and sub4 >0 and sub5 >0):


    total_marks = sub1 + sub2 + sub3 + sub4 + sub5
    print("total marks : ",total_marks)
    percentage = (total_marks/500)*100
    print("percentage : ",percentage)
    if(percentage >= 90):
        print("Grade : A+")
    elif(percentage >= 75):
        print("Grade : A")
    elif(percentage >= 60):
        print("Grade : B")
    elif(percentage >= 40):
        print("Grade : C")
    else:
        print("Grade : Fail")

else:
    print("value cannot be negative")
print("------------------------------")

