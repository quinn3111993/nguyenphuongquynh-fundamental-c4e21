from turtle import *

quinn = Turtle()

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(len(colors)):
    quinn.color(colors[i])
    angle = 360/(i+3)
    for j in range(i+3):
        quinn.forward(100)
        quinn.left(angle)

mainloop()