from matplotlib import pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()
plt.ylim(-10,10)
plt.xlim(-10,10)

def draw_point(x,y):
    plt.scatter(x, y, s=2, c="black")

def redraw():
    # redraw
    fig.canvas.draw()
    fig.canvas.flush_events()

def draw_circle(x,y,r):
    # HERE IS WHERE YOU PUT ALL YOUR MAGIX:
    draw_point(x,y) # <<< as a demo we just draw a point in the center ...
    # probably go in a for loop here
    # calling draw_point(..., ...) at each point of the circle

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

    # this get's triggered on mouse click - call the circle drawing from here:
    r = 1.0
    draw_circle(event.xdata, event.ydata,r)
    redraw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
