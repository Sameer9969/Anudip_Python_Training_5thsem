"""Creates a python program to user which provide 2d figure circle 
rectangle and square after selecting the figure the user again ask
type of corresponding data from the figure after input of corresponding
data again provide a menu to select the operation area,perimeterand as 
per the data provided by user or operation selected by user display the 
result of operation. This task will be repeated again and again until 
user select option to exit from that figure
"""

"""area and perimeter of a rectangle """
def rectangle(lenght,breath):
    area=lenght*breath
    perimeter=2*(lenght+breath)
    return area,perimeter
"""area and perimeter of a circle"""
def circle(radius):
    area=3.14*radius*radius
    perimeter=2*3.14*radius
    return area,perimeter
"""area and perimeter of a square"""
def square(side):
    area=side*side
    perimeter=4*side
    return area,perimeter
"""area and perimeter of a triangle"""
def triangle(base,height):
    area=0.5*base*height
    perimeter=3*base
    return area,perimeter

