# write a program to check whether the given angle can form a triangle or not and if form a triangle the which type of triangle is it
#INPUT OF THREE ANGLES OF A TRIANGLE
angle1 = int(input("Enter the first angle of the triangle: "))
#validation of the angle
if(angle1<0):
    exit("angle cannot be negative.....EXITED")
print("----------------------------------------")
angle2 = int(input("Enter the second angle of the triangle: "))
#validation of the angle
if(angle2<0):
    exit("angle cannot be negative.....EXITED")
print("----------------------------------------")
angle3 = int(input("Enter the third angle of the triangle: "))
#validation of the angle
if(angle3<0):
    exit("angle cannot be negative.....EXITED")
print("----------------------------------------")
#--------------------------------
#--------------------------------
#verifing triangle is form or not
if(angle1 + angle2 + angle3 == 180):
    print("The given angles can form a triangle")
    if(angle1<90 and angle2<90 and angle3<90):
        print("the triangle is an acute triangle")
    elif(angle1==90 or angle2==90 or angle3==90):
        print("the triangle is a right angle triangle")
    else:
        print("the triangle is obtuse triangle")
else:
    print(" The given angles cannot form a triangle")
print("----------------------------------------")