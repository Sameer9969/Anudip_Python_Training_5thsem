"""2. Rectangle Calculator (Basic) 
Problem Statement: 
Create a Rectangle class with attributes length and breadth. 
Implement methods to: 
• Calculate the area.  
• Calculate the perimeter.  
• Display the dimensions and results.  
Sample Output: 
Length     : 12 
Breadth    : 8 
Area       : 96 
Perimeter  : 40 """
#area and perimeter of reactangle 
class Rectangle:
    def __init__(self,lenght,breath):
        self.lenght=lenght
        self.breath=breath

    #area of rectangle
    def area(self):
        area = self.lenght*self.breath
        print("area of rectangle is :",area,"sq.cm")
    
    #perimeter of rectangle
    def perimeter(self):
        perimeter = 2*(self.lenght+self.breath)
        print("perimeter of rectangle is :",perimeter,"cm")

#---------------------main manu-------------------------
while(True):
    print("---------main manu----------")
    print(" 1. for area")
    print(" 2. for perimeter")
    print(" 3. for exit")

    choice=float(input("enter your choice:"))

    if choice==1:
        lenght=float(input("enter lenght:"))
        breath=float(input("enter breath:"))
        rectangle=Rectangle(lenght,breath)
        rectangle.area()

    elif choice == 2:
        lenght=float(input("enter lenght:"))
        breath=float(input("enter breath:"))
        rectangle = Rectangle(lenght,breath)
        rectangle.perimeter()
    else:
        exit("exexted successfully")