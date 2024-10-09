import math

class Circle:
    def __init__(self, radius, diameter, area, circumference):
        self.radius = radius
        self.diameter = diameter
        self.area = area
        self.circumference = circumference

    radius = int(input("Enter the radius of the circle: "))
    @staticmethod
    def diameter(radius):
        return 2 * radius
    
    @staticmethod
    def circumference(diameter):
        return math.pi * diameter
    
    @staticmethod
    def area(radius):
        return math.pi * pow(radius, 2)
    
    @staticmethod
    def semiArea(area):
        return area / 2

cir_radius = Circle.radius
cir_diameter = Circle.diameter(cir_radius)
cir_circumference = Circle.circumference(cir_diameter)
cir_area = Circle.area(cir_radius)
semi_area = Circle.semiArea(cir_area)

print(
    "Properties of a circle\n"
    f"Radius: {cir_radius}\n"
    f"Diameter: {cir_diameter}\n"
    f"Circumference: {round(cir_circumference, 2)}\n"
    f"Area: {round(cir_area,2)}\n"
    f"Semi Area: {round(semi_area,2)}\n"
)

