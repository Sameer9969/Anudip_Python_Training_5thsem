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

