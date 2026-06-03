# PROGRAM TO CALCULATE THE AREA AND PERIMETER OF A TRIANGLE
#INPUT OF THREE SIDES OF A TRIANGLE
print("-----TRIANGLE AREA AND PERIMETER CALCULATOR-----")
side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle:"))
side3 = int(input("Enter the third side of the triangle:"))
#----------------------------------------
print("----------------------------------------")
print("first side: ", side1,"cm")
print("second side: ", side2,"cm")
print("third side: ", side3,"cm")
print("----------------------------------------")
#CALCULATING THE PERIMETER OF THE TRIANGLE
perimeter = side1 + side2 + side3
#----------------------------------------
#CALCULATING THE AREA OF THE TRIANGLE USING HERON'S FORMULA
s = perimeter / 2

#----------------------------------------
#OUTPUT OF THE AREA AND PERIMETER OF THE TRIANGLE
print("The perimeter of the triangle is: ", perimeter,"cm")
print("The area of the triangle is: ", (s * (s - side1) * (s - side2) * (s - side3)) **0.5,"sq.cm")
#----------------------------------------


