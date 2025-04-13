import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Setup turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)

# Define rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def draw_rainbow_flower():
    for i in range(36):
        pen.color(colors[i % len(colors)])
        for _ in range(2):
            pen.circle(100, 60)
            pen.left(120)
        pen.left(10)

draw_rainbow_flower()
pen.hideturtle()
screen.mainloop()