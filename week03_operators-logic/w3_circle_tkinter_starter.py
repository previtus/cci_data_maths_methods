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
    # HERE IS WHERE YOU PUT ALL YOUR MAGIX:
    draw_point(x,y) # <<< as a demo we just draw a point in the center ...
    # probably go in a for loop here
    # calling draw_point(..., ...) at each point of the circle
	
def click(event):
    x, y = event.x, event.y
    print('Clicked at {}, {}'.format(x, y))

    r = 100
    draw_circle(x,y,r)


#root.bind('<Motion>', click) # < this binds it to every movement of the mouse
root.bind('<Button-1>', click) # < this binds it to every click of the mouse button
root.mainloop()

