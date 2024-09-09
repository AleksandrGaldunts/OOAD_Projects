# Bridge Design pattern


"""
 
    Bridge֊ը structural design pattern է,  որը բաժանում է`  abstraction (high-level logic),
     implementation (low-level logic), որոնք կարող են մշակվել միմյանցից անկախ

"""
import math


class AreaCalculator:
    def calculate_area(self):
        pass

class SquareAreaCalculator(AreaCalculator):
    def __init__(self, x):
        self.x = x

    def calculate_area(self):
        return self.x ** 2

class CircleAreaCalculator(AreaCalculator):
    def __init__(self, x):
        self.x = x

    def calculate_area(self):
        return math.pi * (self.x ** 2)

class Shape:
    def __init__(self, area_calculator):
        self.area_calculator = area_calculator

    def area(self):
        return self.area_calculator.calculate_area()


square_area_calculator = SquareAreaCalculator(2)
square = Shape(square_area_calculator)
print(f"Square area = {square.area()}")
circle_area_calculator = CircleAreaCalculator(2)
circle = Shape(circle_area_calculator)
print(f"Circle area = {circle.area()}")
