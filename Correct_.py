def draw_design():
    turtle.speed(2)
    turtle.pensize(2)
    turtle.color("blue")

    # Draw a square 
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def display_message():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.clear()
    turtle.write("Correct! Got it right", align="center", font=("Arial", 16, "normal"))

import turtle

# Set up the turtle window
turtle.title("Turtle Correct Message with Simple Design")
turtle.bgcolor("lightblue")

# Draw the design
draw_design()

# Display the message
display_message()

# Keep the window open
turtle.done()
