import turtle as t
import random

tim = t.Turtle()

########### Dragon Age Random Walk ########

dragon_age_colours = [
    "#0B0B0B",  # Crow black
    "#8B0000",  # deep Antivan red
    "#FFD700",  # gold (Crow/royal accents)
    "#4B0082",  # Tevinter purple
    "#800080",  # arcane purple
    "#1F3A5F",  # Warden blue
    "#2F4F4F",  # dark slate (armor tones)
    "#0B6623",  # Dalish green
    "#228B22",  # forest green
    "#00BFFF",  # lyrium blue
    "#00FFFF",  # Fade cyan
]

directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(dragon_age_colours))
    tim.setheading(random.choice(directions))
    tim.forward(30)

screen = t.Screen()
screen.exitonclick()