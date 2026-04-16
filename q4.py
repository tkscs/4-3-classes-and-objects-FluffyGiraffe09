import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.dot()
        turtle.penup()
        turtle.write(self)
point_1 = Point(0, 0)
point_2 = Point(100, 0)
point_3 = Point(100, 100)
point_4 = Point(0, 100)

print(point_1)
print(point_2)
print(point_3)
print(point_4)

point_1.draw()
point_2.draw()
point_3.draw()
point_4.draw()


turtle.exitonclick()