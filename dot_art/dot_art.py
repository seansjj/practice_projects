import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
cursor = Turtle()

# list of possible colors for the painting
color_list = [(2, 9, 30), (244, 238, 243), (122, 95, 42), (71, 32, 22), (237, 211, 72), (220, 81, 60), (225, 118, 100), (92, 2, 21), (178, 140, 170), (150, 92, 114), (34, 90, 27), (9, 153, 73), (204, 64, 92), (167, 129, 77), (2, 64, 147), (3, 78, 28), (5, 220, 217), (220, 179, 218), (79, 135, 179), (122, 153, 178), (79, 112, 141), (119, 185, 167), (7, 218, 224), (120, 14, 33), (132, 223, 210), (241, 204, 9), (230, 173, 165)]

cursor.speed(10)
cursor.penup()


def paint_forward(steps):
    for dot in range(steps):
        random_colour = random.choice(color_list)

        cursor.dot(20, random_colour)
        cursor.forward(25)


def paint_2rows(double_rows):
    for paint in range(double_rows):
        paint_forward(9)
        cursor.left(90)
        paint_forward(1)
        cursor.left(90)
        paint_forward(9)
        cursor.right(90)
        paint_forward(1)
        cursor.right(90)

        
paint_2rows(5)








screen = Screen()
screen.exitonclick()
