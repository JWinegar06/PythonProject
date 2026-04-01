import turtle as t
import random

screen = t.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Dragon Age Spirograph")

tim = t.Turtle()
tim.speed("fastest")
tim.width(2)
tim.hideturtle()

t.colormode(255)

# Dragon Age inspired palette
dragon_age_colors = [
    (139, 0, 0),      # dark red
    (178, 34, 34),    # firebrick
    (212, 175, 55),   # gold
    (192, 192, 192),  # silver
    (34, 85, 34),     # deep green
    (72, 61, 139),    # dark slate blue
    (105, 105, 105),  # dim gray
    (160, 82, 45),    # brown
    (25, 25, 25),     # near black
    (220, 20, 60),    # crimson
]

def dragon_age_color():
    return random.choice(dragon_age_colors)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(dragon_age_color())
        tim.circle(120)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()