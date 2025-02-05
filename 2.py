class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

s = Shape()
print(s.area())
s = Square(int(input()))
print(s.area())