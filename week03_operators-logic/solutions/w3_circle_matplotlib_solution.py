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
    for t in range(0, 360):
        t_radians = float(t) * math.pi / 180.0
        x_point = r * math.cos(t_radians) + x
        y_point = r * math.sin(t_radians) + y
        draw_point(x_point,y_point)


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
