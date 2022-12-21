from src.Figure import Figure

class Square(Figure):
    def __init__(self, name, a):
        if not a > 0:
            raise ValueError
        self.a = a

        self.name = name

    def perimeter(self):
        return self.a + self.a + self.a + self.a

    #@property
    def area(self):
        return self.a * self.a