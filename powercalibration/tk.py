#view using the matfig model and a generic button controller
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matfig import matfig
from controller import controller
import numpy as np

global canvas,newfig,shit

window = tk.Tk()
window.wm_title("buelaebcubeuaohubauh")

x = np.array([1,2,3,6,1])
y = np.array([2,5,2,1,2])

newfig = matfig(x,y)
newfig.dummy()
action = controller(newfig)

canvas = FigureCanvasTkAgg(newfig.fig, master=window)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)

#button clicked - data taken, passed to a model
def add():
    action.add(ent1.get(),ent2.get())
    newfig.dummy() #updates axes
    print(newfig.x,newfig.y) #debug
    canvas.draw() #updates view

row = tk.Frame(master=window)
# v = tk.StringVar()
ent1 = tk.Entry(row)
ent2 = tk.Entry(row)
but = tk.Button(row, text="add x,y", command=add)
row.pack(side=tk.BOTTOM, fill = tk.X, padx=5, pady=5)
ent1.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
ent2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
but.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=5, pady=5)

quitButton = tk.Button(master=window, text="quit", command=window.quit)
quitButton.pack(side=tk.BOTTOM)

canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
tk.mainloop()
