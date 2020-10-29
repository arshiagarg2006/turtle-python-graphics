from turtle import *
from random import randint


ruby = Turtle()
ruby.color('red')
ruby.shape('turtle')
ruby.penup()
ruby.goto(-160, 100)
ruby.pendown()

for turn in range(10):
    ruby.right(36)

lily = Turtle()
lily.color("blue")
lily.shape('turtle')
lily.penup()
lily.goto(-160, 70)
lily.pendown()

for turn in range(72):
    lily.left(5)

tooga = Turtle()
tooga.color('green')
tooga.shape('turtle')
tooga.penup()
tooga.goto(-160, 40)
tooga.pendown()

for turn in range(60):
    tooga.right(6)

oru = Turtle()
oru.color('orange')
oru.shape('turtle')
oru.penup()
oru.goto(-160, 10)
oru.pendown()

for turn in range(30):
    oru.left(12)

for turn in range(70):
    ruby.forward(randint(3, 8))
    lily.forward(randint(3, 8))
    tooga.forward(randint(3, 8))
    oru.forward(randint(3, 8))

