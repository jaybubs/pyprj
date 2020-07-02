import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

window = tk.Tk()

form = tk.Frame(relief=tk.SUNKEN,borderwidth=3)
form.pack()

labels = ["A", "B", "C"]

for idx, text in enumerate(labels):
    label = tk.Label(master=form, text=text)
    entry = tk.Entry(master=form, width=50)
    label.grid(row=idx, column=0, sticky="e")
    entry.grid(row=idx, column=1)

buttons = tk.Frame()
buttons.pack(fill=tk.X, ipadx=5, ipady=5)

but = ["cock", "pussy", "dick"]

for shit, text in enumerate(but):
    butty = tk.Button(master=buttons, text=text)
    butty.pack(side=tk.RIGHT, padx=10, ipadx=10)

window.mainloop()
