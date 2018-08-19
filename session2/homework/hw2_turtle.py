from turtle import *

quinn = Turtle()

#first shape
quinn.color("red")
quinn.left(30)
for i in range(4):
    quinn.forward(100)
    quinn.right(60)
    quinn.forward(100)
    quinn.right(120)
    quinn.forward(100)
    quinn.right(60)
    quinn.forward(100)
    quinn.right(30)

#move to draw new shape
quinn.penup()
quinn.right(30)
quinn.forward(300)
quinn.pendown()

#second shape
for i in range(3,7):
    angle = 360/i
    if i % 2 == 0:
        quinn.color("red")
    else:
        quinn.color("blue")
    for j in range(i):
        quinn.forward(100)
        quinn.left(angle)

mainloop()