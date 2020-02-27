import tkinter as tk
import math 

root = tk.Tk()
root.title("Drawing")
canvas_width = 1000
canvas_height = 1000
w = tk.Canvas(root,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=tk.YES, fill=tk.BOTH)


def draw_point(x,y):
    w.create_oval((x - 1), (y - 1), (x + 1), (y + 1), fill="#476042")

def draw_circle(x,y,r):
    for t in range(0, 360):
        t_radians = float(t) * math.pi / 180.0
        x_point = r * math.cos(t_radians) + x
        y_point = r * math.sin(t_radians) + y
        draw_point(x_point,y_point)

def click(event):
    x, y = event.x, event.y
    print('Clicked at {}, {}'.format(x, y))

    r = 100
    draw_circle(x,y,r)


#root.bind('<Motion>', click) # < this binds it to every movement of the mouse
root.bind('<Button-1>', click) # < this binds it to every click of the mouse button
root.mainloop()

