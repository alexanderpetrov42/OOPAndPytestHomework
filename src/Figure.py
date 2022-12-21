class Figure:
    def __init__(self, name):
        self.name = name
    def add_area(self, figure):
        fl = ["Circle", "Rectangle", "Square", "Triangle"]
        if type(figure).__name__ in fl:
            return self.area() + figure.area()
        else:
           return ValueError