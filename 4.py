import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, change_x, change_y):
        self.x += change_x
        self.y += change_y
    def dist(self, second_point):
        return math.sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2)

p1 = Point(int(input()), int(input()))
p2 = Point(int(input()), int(input()))
p1.show()
p2.show()
p1.move(int(input()), int(input()))
p2.move(int(input()), int(input()))
print(p1.dist(p2))
