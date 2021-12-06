import turtle

class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        p = Point(-100, 100, "blue")
        p.draw()
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        turtle.dot()
class Box():
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        b = Box(130, 140, 70, 60, "Red")
    
    def draw_action(self):
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(60)
class BoxFilled():
    def __init__(x1, y1, weidth, height, color):
        super().__init__()
        b = BoxFilled(1,2,3,4."Blue","Red")
        Box.draw_action(self)
        

