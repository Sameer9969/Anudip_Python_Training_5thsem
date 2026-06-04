# a teacher recording the attendence of strenght of class ic 30 every time 
#every time they need to insert the student is present or absent so count the total number of student is present or absent

#--------------------------------
student = 1
while(student <= 30):
    attendence = input("Is student present or absent? (P/A) : ")
    if(attendence == 'P' or attendence == 'p'):
        print("Student", student, "is present.")
    elif(attendence == 'A' or attendence == 'a'):
        print("Student", student, "is absent.")
    else:
        print("Invalid input. Please enter 'P' for present or 'A' for absent.")
    student +=1
    print("--------------------------------")

