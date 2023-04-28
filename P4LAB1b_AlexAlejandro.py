import turtle

# Create a turtle object
a = turtle.Turtle()

# Set the pen color and size
a.pencolor('purple')
a.pensize(5)

# Draw the first initial
a.right(60)
a.forward(200)
a.backward(200)
a.left(-60)
a.forward(195)
a.backward(85)
a.left(120)
a.forward(105)

# Move to the right and lower the pen to draw the second initial
a.penup()
a.goto(195, 0)
a.pendown()

# Draw the second initial
a.right(60)
a.forward(200)
a.backward(200)
a.left(-60)
a.forward(195)
a.backward(85)
a.left(120)
a.forward(105)

# Hide the turtle cursor
a.hideturtle()

# Wait for the user to close the window
turtle.done()
