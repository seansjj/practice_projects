import random
import turtle
from turtle import Screen, Turtle

cursor = Turtle()
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colour = (r, g, b)

    return colour


cursor.speed(0)
rotation = 0

for _ in range(60):
    cursor.pencolor(random_colour())
    cursor.circle(100)
    rotation += 1
    cursor.setheading(6 * rotation)

screen = Screen()
screen.exitonclick()
