"""Creates a python program to user which provide 2d figure circle 
rectangle and square after selecting the figure the user again ask
type of corresponding data from the figure after input of corresponding
data again provide a menu to select the operation area,perimeterand as 
per the data provided by user or operation selected by user display the 
result of operation. This task will be repeated again and again until 
user select option to exit from that figure
"""
from figure import *
while True: 

    print("\n===== Figure Menu =====")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    figure_choice = int(input("Enter your choice: "))

    if figure_choice == 4:
        print("Thank You for using Geometry Calculator.")
        break

    # Circle
    if figure_choice == 1:
        radius = float(input("Enter Radius: "))

        if radius <= 0:
            print("Radius must be positive.")
            continue

        while True:
            print("\n----- Operation Menu -----")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = int(input("Enter your choice: "))

            if op == 1:
                print("Area of Circle =", area_circle(radius))

            elif op == 2:
                print("Perimeter of Circle =", perimeter_circle(radius))

            elif op == 3:
                break

            else:
                print("Invalid Choice")

    # Square
    elif figure_choice == 2:
        side = float(input("Enter Side: "))

        if side <= 0:
            print("Side must be positive.")
            continue

        while True:
            print("\n----- Operation Menu -----")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = int(input("Enter your choice: "))

            if op == 1:
                print("Area of Square =", area_square(side))

            elif op == 2:
                print("Perimeter of Square =", perimeter_square(side))

            elif op == 3:
                break

            else:
                print("Invalid Choice")

    # Rectangle
    elif figure_choice == 3:
        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))

        if length <= 0 or breadth <= 0:
            print("Length and Breadth must be positive.")
            continue

        while True:
            print("\n----- Operation Menu -----")
            print("1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            op = int(input("Enter your choice: "))

            if op == 1:
                print("Area of Rectangle =", area_rectangle(length, breadth))

            elif op == 2:
                print("Perimeter of Rectangle =", perimeter_rectangle(length, breadth))

            elif op == 3:
                break

            else:
                print("Invalid Choice")

    else:
        print("Invalid Figure Choice")

    choice = input("\nDo you want to continue using the application? (Y/N): ")

    if choice.upper() != "Y":
        print("Thank You for using Geometry Calculator.")

        
        break