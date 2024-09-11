"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')

tina.pencolor('red')
tina.forward(50)
tina.left(120)

tina.pencolor('yellow')
tina.forward(50)
tina.left(120)

tina.pencolor('blue')
tina.forward(50)
tina.left(120)


... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
