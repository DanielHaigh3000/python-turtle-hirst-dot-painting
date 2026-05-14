from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
color_list = [(236, 35, 108), (145, 28, 66), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), (170, 191, 221), (114, 10, 8)]

screen.colormode(255)

def draw_hirst(rows,cols):
  # Initialize the x and y coordinates
  x_coord = -100
  y_coord = -100

  # Lift pen up since we don't need it for dots
  tim.penup()

  # Hide the turtle
  tim.hideturtle()

  # Control the columns
  for _ in range(cols):
    # Move to coords
    tim.setpos(x_coord,y_coord)

    # Control the rows
    for _ in range(rows):
      # Draw a dot row
      tim.dot(20,random.choice(color_list))
      tim.forward(50)

    # Adjust the y value for the next column
    y_coord += 50

draw_hirst(10,10)
screen.exitonclick()