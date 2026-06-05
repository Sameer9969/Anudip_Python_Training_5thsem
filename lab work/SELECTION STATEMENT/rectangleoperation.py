#wirite a program to find the area and perimeter of rectangle (if validate)
#INPUT OF LENGTH AND BREADTH OF THE RECTANGLE
print("-----RECTANGLE AREA AND PERIMETER CALCULATOR-----")
len = float(input("Enter the length of the rectangle: "))
bre = float(input("Enter the breadth of the rectangle: "))
#-----------------------------------------
print("----------------------------------------")
print("length: ", len,"cm")
print("breadth: ", bre,"cm")
print("----------------------------------------")
#VALIDATION OF THE LENGTH AND BREADTH
if(len<0 ):
    exit("length and breadth cannot be negative.....EXITED")
if(bre<0):
    exit("length and breadth cannot be negative.....EXITED")
#-----------------------------------------
#CALCULATING THE PERIMETER OF THE RECTANGLE
perimeter = 2 * (len+bre)
#CALCULATING THE AREA OF THE RECTANGLE
area = len * bre
#-----------------------------------------
print("perimeter of the rectangle is: ", perimeter,"cm")
print("area of the rectangle is : ", area,"sq.cm")
#-----------------------------------------
print("----------------------------------------")