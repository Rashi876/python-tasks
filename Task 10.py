
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def rectangle_area(self):
        return self.length*self.width
l=int(input("Enter length of rectangle: "))
w=int(input("Enter width of rectangle: "))
newRectangle = Rectangle(l, w)
print(newRectangle.rectangle_area())
