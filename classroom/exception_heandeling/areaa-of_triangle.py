"""
Problem Statement: Area of a Triangle Using Three Sides with Exception Handling 
Design a Python program to calculate the area of a triangle using Heron's Formula. The program should 
accept the lengths of the three sides of the triangle from the user and display the calculated area. 
However, the program must handle the following exceptional situations gracefully: 
1. If the user enters a non-numeric value instead of a number for any side, display an appropriate error 
message.  
2. If any of the entered side lengths are zero or negative, inform the user that triangle sides must be 
greater than zero.  
3. If the three entered side lengths cannot form a valid triangle according to the Triangle Inequality 
Theorem, notify the user that the triangle is invalid.  
4. Ensure that the program does not terminate abruptly due to invalid input and provides meaningful 
feedback using exception handling.  
5. Display a message indicating that the triangle area calculation process has been completed, 
regardless of whether the calculation was successful or an exception occurred.  
Note: Use Heron's Formula to calculate the area of the triangle: 
�
�=𝑎+𝑏+𝑐
2 
Area=√𝑠(𝑠−𝑎)(𝑠−𝑏)(𝑠−𝑐)
Problem Statement: Area of a Triangle Using Three Sides with Exception Handling
Design a Python program to calculate the area of a triangle using Heron's Formula.
The program should accept the lengths of the three sides of the triangle from the user
and display the calculated area. It should also handle invalid input safely and always
show that the process has completed.
"""

try:
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    side3 = float(input("Enter the third side of the triangle: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Error: Triangle sides must be greater than zero.")
    elif (side1 + side2 <= side3 or
        side1 + side3 <= side2 or
        side2 + side3 <= side1):
        print("Error: The entered lengths cannot form a valid triangle.")
    else:
        s = (side1 + side2 + side3) / 2
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        print(f"The area of the triangle is: {area:.4f}")

except ValueError:
    print("Error: Please enter numeric values for all three sides.")

finally:
    print("Triangle area calculation process completed.")
