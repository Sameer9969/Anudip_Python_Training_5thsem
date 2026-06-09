import output

while True:
    print("\n===== SHAPE CALCULATOR =====")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Square")
    print("4. Triangle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))

        area, perimeter = output.rectangle(length, breadth)

        print("Area =", area)
        print("Perimeter =", perimeter)

    elif choice == 2:
        radius = float(input("Enter Radius: "))

        area, perimeter = output.circle(radius)

        print("Area =", area)
        print("Perimeter =", perimeter)

    elif choice == 3:
        side = float(input("Enter Side: "))

        area, perimeter = output.square(side)

        print("Area =", area)
        print("Perimeter =", perimeter)

    elif choice == 4:
        base = float(input("Enter Base: "))
        height = float(input("Enter Height: "))

        area, perimeter = output.triangle(base, height)

        print("Area =", area)
        print("Perimeter =", perimeter)

    elif choice == 5:
        print("Program Closed")
        break

    else:
        print("Invalid Choice! Please Try Again.")