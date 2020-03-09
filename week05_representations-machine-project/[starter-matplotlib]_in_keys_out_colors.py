# Using Matplotlib
# to get input from the user (key press)
# and show color as an output (color of the screen)

from matplotlib import pyplot as plt
import sys

fig, ax = plt.subplots()
plt.ylim(-10,10)
plt.xlim(-10,10)

def color(name):
    ax.set_facecolor(name)
    fig.canvas.draw()
    fig.canvas.flush_events()

def press(event):
    global output_color
    # We get this as an input:
    print('input, pressed:', event.key)

    # PLACE YOUR BEHAVIOUR HERE:
    # ps: this is a simple example, which is not using State Machines at all
    if event.key == 'right':
        output_color = "blue"
    if event.key == 'left':
        output_color = "red"

    # This is your output:
    color(output_color)

output_color = "black"


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



fig.canvas.mpl_connect('key_press_event', press)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()