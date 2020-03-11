# Using turtle (and Tkinter)
# to get input from the user (key press)
# and show color as an output (color of the screen)

import turtle
wn=turtle.Screen()
bob=turtle.Turtle()


# PLACE YOUR BEHAVIOUR HERE:
# ps: this is a simple example, which is not using State Machines at all

def left():
   wn.bgcolor('red')

def right():
   wn.bgcolor('blue')

wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")


# <===============================================>
# HINTS:
# State machine should have:
# - state
state = 0
# - alphabet of allowed inputs
alphabet = ["a","b","c"]
# - transitions
#   up to you to implement this!
# - in this case some mapping between what state we are in and what do we want to output (like color)
# <===============================================>


wn.listen()
bob.hideturtle()
turtle.mainloop()