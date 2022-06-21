class Shape:
    def __init(self,color='black',filled=False):
        self.color=color
        self.filled=filled
    def get_color(self):
        return self.color
    def set_color(self):
        self.color=color
    def get_filled(self):
        return set.filled
    def set_filled(self):
        set.filled=filled
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length=length
        self.breadth=breadth
    def get_length(self):
        return self.length
    def set_length(self,length):
        self.length=length
    def get_breadth(self):
        return self.breadth
    def set_breadth(self,breadth):
        self.breadth=breadth
    def get_area(self):
        return self.length*self.breadth
    def get_perimeter(self):
        return 2*(self.length*self.breadth)

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    def get_radius(self):
        return self.radius
    def set_radius(self,radius):
        self.radius=radius
    def get_area(self):
        return 3.14*self.radius**2
    def get_perimeter(self):
        return 2*3.14*self.radius

length=float(input())
breadth=float(input())
r1=Rectangle(length,breadth)
print("Area of Rectangle:",r1.get_area())
print("Perimeter of Rectangle:",r1.get_perimeter())
print("Color of Rectangle:",r1.get_color())
print("Rectangle is Filled:",r1.get_filled())
r1.set_filled(True)
print("Rectangle is Filled:",r1.get_filled())
r1.set_color("Brown")
print("Color of Rectangle:",r1.get_color())

radius=float(int(input()))
c1=Circle(radius)
print("Area of Circle:",c1.get_area())
print("Perimeter of Circle:",c1.get_perimeter())
print("Color of Circle:",c1.get_color())
print("Circle is Filled:",c1.get_filled())
c1.set_filled(True)
print("Circle is Filled:",c1.get_filled())
c1.set_color("Green")
print("Color of Rectangle:",c1.get_color())