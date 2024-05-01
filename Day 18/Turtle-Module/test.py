import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(4)
turtle.colormode(255)

# drawing a square
for _ in range(0, 4):
    timmy.forward(100)
    timmy.right(90)

turtle.resetscreen()

# drawing a dashed line
timmy.speed(3)
i = 0
while i < 10:
    if i % 2 == 0:
        timmy.pendown()
        timmy.forward(10)
        i += 1
    if i % 2 != 0:
        timmy.penup()
        timmy.forward(10)
        i += 1

turtle.resetscreen()

# drawing triangle, square, pentagon, hexagon, heptagon, octagon
# nonagon and decagon
timmy.speed(3)
colors = ["#781F19", "#E7EBDA", "#C7B446", "#1B5583", "#7D8471",
          "#763C28", "#FAD201", "#6A5D4D"]

sides = [3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, 8):
    timmy.pencolor(colors[i])
    timmy.pensize(4)
    distance = 100
    angle = 360 / sides[i]
    for _ in range(0, sides[i]):
        timmy.right(angle)
        timmy.forward(distance)

turtle.resetscreen()

# drawing a random walk
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


directions = [0, 90, 180, 270]
for _ in range(100):
    timmy.pensize(4)
    timmy.pencolor(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

turtle.resetscreen()

# drawing a spirograph
timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()


