import math
class Polar:
    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle

    def __repr__(self):
        return f"Polar({self.radius}, {self.angle})"

    def __add__(self, other):
        x1 = self.radius * math.cos(math.radians(self.angle))
        y1 = self.radius * math.sin(math.radians(self.angle))
        x2 = other.radius * math.cos(math.radians(other.angle))
        y2 = other.radius * math.sin(math.radians(other.angle))

        x = x1 + x2
        y = y1 + y2

        radius = math.sqrt(x ** 2 + y ** 2)
        angle = math.degrees(math.atan2(y, x))

        angle = angle % 360

        return Polar(radius, angle)


p1 = Polar(4, 60)
p2 = Polar(2, 30)

result = p1 + p2
print(result)
