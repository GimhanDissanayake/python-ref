import turtle
import math
import tkinter

# Create turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)
pen.color("red", "yellow")

def draw_flower():
    pen.begin_fill()
    for _ in range(36):
        for _ in range(2):
            pen.circle(100, 60)
            pen.left(120)
        pen.left(10)
    pen.end_fill()

draw_flower()
pen.hideturtle()
screen.mainloop()
