class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    

radius=float(input("Enter radius of circle: "))
circle = Circle(radius)
print(f"Area of circle is {circle.area()} \n")
print(f"Perimeter of circle is {circle.perimeter()}")
