# write a program to check whether the given angle can form a triangle or not
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
else:
    print(" The given angles cannot form a triangle")
print("----------------------------------------")