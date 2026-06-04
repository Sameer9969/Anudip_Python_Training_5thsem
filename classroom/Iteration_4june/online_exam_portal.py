#Write a program that accepts marks from the user and continues asking for marks until the entered score is 40 or more. 
#Display a congratulatory message once the student passes the assessment.
#--------------------------------


marks = 0
while(True):
    student_marks = int(input("Enter your marks: "))
    if(student_marks >= 40):
        print("result : passed")
        print("Congratulations! You have passed the assessment.")
        break
    else:
        print("result : fail")
    print("------------------------------")