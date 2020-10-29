import turtle
turtle.Screen().bgcolor("black")

turtle_stamp = turtle.Turtle()
turtle_stamp.shape('turtle')

turtle.Screen().colormode(255)
turtle_stamp.color(121, 186, 78)
turtle_stamp.penup()
turtle_stamp.left(90)
turtle_stamp.forward(100)
turtle_stamp.right(90)
turtle_stamp.forward(100)
turtle_stamp.stamp()
turtle_stamp.left(90)
turtle_stamp.forward(100)
turtle_stamp.stamp()
turtle_stamp.left(90)
turtle_stamp.forward(100)
turtle_stamp.stamp()
turtle_stamp.left(90)
turtle_stamp.forward(100)
turtle_stamp.stamp()


turtle_stamp = turtle.Turtle()
turtle_stamp.shape('turtle')
turtle_stamp.penup()
turtle.colormode(255)
turtle_stamp.back(300)

red = (235, 73, 113)
orange = (237, 109, 24)
yellow = (252, 231, 91)
green = (57, 191, 23)
blue = (23, 143, 191)
violet = (183, 96, 214)
color = [red, orange, yellow, green, blue, violet]

for m in range(6):
    turtle_stamp.forward(30)
    turtle_stamp.color(color[m]);
    turtle_stamp.stamp()
    
