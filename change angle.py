import turtle               
from itertools import cycle
colors = cycle(['red', 'orange', 'green', 'yellow', 'blue', 'pink'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+10, angle+10,shift+1)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(40,5,5)
