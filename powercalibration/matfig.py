#dummy model for a couple of graphs, for controller design purposes
import numpy as np
from matplotlib.figure import Figure
import matplotlib.gridspec as gridspec

class matfig():
    gs = gridspec.GridSpec(2,1, height_ratios=[1,1])

    def __init__(self, x, y):
        # self.figure = Figure()
        self.fig = Figure()
        self.x = x
        self.y = y

        self.ax1 = self.fig.add_subplot(self.gs[0])
        self.ax2 = self.fig.add_subplot(self.gs[1])

        self._time = None

    def time(self,a,b, step):
        self._time = np.arange(a,b,step)
        return self._time

    def dummy(self):
        return self.ax1.plot(self.x,self.y), self.ax2.plot(self.y,self.x)
    
    def draw(self):
        return self.fig

    def hello(self):
        print("hello")

    def addPoint(self, entity1, entity2):
        self.x = np.append(self.x, entity1)
        self.y = np.append(self.y, entity2)
