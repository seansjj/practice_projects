import random
import turtle
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Enter a colour: ')
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
starting_y = 150
all_turtles = []

for colour in colours:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_y)
    starting_y -= 60
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f'You win! The winning turtle is {winning_colour}')
            else:
                print(f'You lose. The winning turtle is {winning_colour}')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
