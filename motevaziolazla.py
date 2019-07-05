import math


class CalculateArea:
    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha

    def calculate_area(self):
        area = self.a * self.calculate_height()
        return area

    def calculate_height(self):
        height = self.b * math.sin(math.radians(self.alpha))
        return height


p = CalculateArea(10, 5, 30)

print(p.calculate_area())
