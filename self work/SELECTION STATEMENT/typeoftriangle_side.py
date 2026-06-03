#write a program to check wheather all three side of triangle are forming a triangle or not and if forming then find the type of triangle
#INPUT OF THREE SIDES OF A TRIANGLE
print("-----TRIANGLE FORMATION CHECKER-----")
side1 = int(input("Enter the first side of the triangle: "))
#validation of the side
if(side1<0):
    exit("side cannot be negative. . . . . .EXITED ")
    #----------------------------------------

side2 = int(input("Enter the second side of the triangle: "))
#validation of the side
if(side2<0):
    exit("side cannot be negative. . . . . .EXITED ")
    #----------------------------------------

side3 = int(input("Enter the third side of the triangle: "))
#validation of the side
if(side3<0):
    exit("side cannot be negative. . . . . .EXITED ")

#----------------------------------------
print("----------------------------------------")
print("first side: ", side1,"cm")
print("second side: ", side2,"cm")  
print("third side: ", side3,"cm")
print("----------------------------------------")
#--------------------------------
#verifing triangle is form or not
if(side1 +side2 > side3 and side1 + side3 >side2 and side2 + side3 > side1):
    print("The given sides can form a triangle")
    if(side1==side2==side3):
        print("the triangle is an equilateral triangle")
    elif(side1==side2 or side2==side3 or side1==side3):
        print("the triangele is an isosceles triangle")
    else:
        print("the triangle is scalene triangle")
else:
    print(" The given sides cannot form a triangle")
print("----------------------------------------")
