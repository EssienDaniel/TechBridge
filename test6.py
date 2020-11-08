
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.pi = math.pi
    def calculatePerimeter(self):
        return ("The perimeter of the circle is {}com".format(2*self.pi*self.radius))
    
    def calculateArea(self):
        return ("The area of the circle is {} square".format(math.pi*self.radius**2))


c = Circle(5)

print(c.calculatePerimeter())


