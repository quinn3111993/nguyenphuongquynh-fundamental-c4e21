from turtle import *

quinn = Turtle()
quinn.color("green", "yellow")
quinn.speed(0)

#1. A square:

quinn.begin_fill()
for i in range(4):
    quinn.forward(100)
    quinn.left(90)

#Move to draw new shape:

quinn.penup()
quinn.forward(150)
quinn.pendown()

#2. An equilateral triangle:

for i in range(3):
    quinn.forward(100)
    quinn.left(120)

#Move to draw new shape:

quinn.penup()
quinn.forward(200)
quinn.pendown()

#3. A circle

quinn.circle(50)
quinn.end_fill()

#Move to draw new shape:

quinn.penup()
quinn.forward(150)
quinn.left(90)
quinn.forward(50)
quinn.right(90)
quinn.pendown()

#4. Multi-circle:

for i in range(36):
    quinn.circle(25)
    quinn.left(10)

mainloop()