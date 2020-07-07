import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import PySimpleGUI as sg
import matplotlib
# from matplotlib.figure import Figure
from calibrate import calibrate

# ------------------------------- START OF YOUR MATPLOTLIB CODE -------------------------------

sp1 = (241)
sp2 = (243)
x = np.arange(0, 3, .01)
y = 2 * np.sin(2 * np.pi *x)

fig = calibrate()

# ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

# ------------------------------- Beginning of Matplotlib helper code -----------------------
matplotlib.use('TkAgg')
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    toolbar = NavigationToolbar2Tk(figure_canvas_agg, canvas)
    toolbar.update()
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# ------------------------------- Beginning of GUI CODE -------------------------------

# define the window layout
layout = [[sg.Text('Plot test')],
          [sg.Canvas(key='-CANVAS-')],
          [sg.Button('Ok')]]

# create the form and show it without the plot
window = sg.Window('Matplotlib Single Graph', layout, location=(0,0), finalize=True, element_justification='center', font='Helvetica 18')

window.maximize()
# add the plot to the window
draw_figure(window['-CANVAS-'].TKCanvas, fig.draw())

event, values = window.read()
window.close()
