import random
from turtle import Screen, Turtle

cursor = Turtle()
angle = [0, 90, 180, 270]
colours = ['blue', 'red', 'green', 'yellow']

cursor.width(5)

for turtle in range(20):
    cursor.pencolor(random.choice(colours))
    cursor.right(random.choice(angle))
    cursor.forward(25)

# random walk
# line thick
# speed up

screen = Screen()
screen.exitonclick()
