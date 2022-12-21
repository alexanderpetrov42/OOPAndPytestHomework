from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self,name, a, b):
        if not a > 0 or not b > 0:
            raise ValueError
        self.a = a
        self.b = b

        self.name = name

    def perimeter(self):
        return 2*(self.a+self.b)

    def area(self):
        return self.a * self.b