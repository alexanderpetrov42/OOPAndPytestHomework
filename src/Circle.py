from src.Figure import Figure
class Circle(Figure):
    def __init__(self, name, r):
        if not r > 0:
            raise ValueError
        self.r = r
        self.pi = 3.14

        self.name = name
    def perimeter(self):
        return 2 * self.pi * self.r

    #@property
    def area(self):
        return self.pi * self.r * self.r