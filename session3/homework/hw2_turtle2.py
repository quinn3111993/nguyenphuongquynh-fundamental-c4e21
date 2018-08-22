from turtle import *

quinn = Turtle()

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(len(colors)):
    quinn.color(colors[i])
    quinn.begin_fill()
    for j in range(2):
        quinn.right(90)
        quinn.forward(100)
        quinn.right(90)
        quinn.forward(50)
    quinn.end_fill()
    quinn.penup()
    quinn.forward(50)
    quinn.pendown()

mainloop()