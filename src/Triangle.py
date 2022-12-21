from src.Figure import Figure
from src.Circle import Circle
class Triangle(Figure):
    def __init__(self, name, a, b, c):
        if not a > 0 or not b > 0 or not c > 0:
            raise ValueError
        self.a = a
        self.b = b
        self.c = c

        self.name = name

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter()
        s=s/2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5