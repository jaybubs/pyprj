from sys import argv
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from calibrate import calibrate
from controller import controller
import numpy as np
from matplotlib.figure import Figure

from calibrate import calibrate

files = [] #to supply csvs
for argument in argv[1:]:
    files.append(argument)

window = tk.Tk()
newfig = calibrate(*files)

canvas = FigureCanvasTkAgg(newfig.fig, master=window)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)

row = tk.Frame(master=window)
test = str(newfig.dotProduct())
quote = "The similarity factor is " + test
text = tk.Text(window, height=1)
text.insert(tk.END, quote)
text.configure(state='disabled')
quitButton = tk.Button(master=window, text="quit", command=window.quit)
quitButton.pack(side=tk.BOTTOM)
text.pack(side=tk.BOTTOM)

canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
tk.mainloop()
