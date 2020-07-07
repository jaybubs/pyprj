import numpy as np
from Csver import Csver
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import AutoMinorLocator
from matplotlib.figure import Figure


def percentile(n, quantity): #n between [0,1]
    return (np.cumsum(quantity) < np.sum(quantity)*n).sum()

class calibrate():
    #fixed for now
    gs = gridspec.GridSpec(2,1, height_ratios=[1,1])
    error = 1
    bins = 50

    def __init__(self, set1='lezynehardknott.csv', set2='tacxhardknott.csv'):
        self.fig  = Figure()
        self.set1 = Csver(set1)
        self.set2 = Csver(set2)
        #force use secs and watts for now
        self.time = self.set1.column('secs')
        self.ma1  = self.set1.movingAverage('watts')
        self.ma2  = self.set2.movingAverage('watts')
        self.mdiff = np.absolute(self.ma1-self.ma2)*100/((self.ma1+self.ma2)/2.0)
        self.maxerr = np.max(self.mdiff)
        self.cock, self.balls = np.histogram(self.mdiff, bins=self.bins, range=(0,self.maxerr))

        self.ax1 = self.fig.add_subplot(self.gs[0])
        self.ax2 = self.fig.add_subplot(self.gs[1])

        self.ax1.plot(self.time, self.ma1, label=set1)
        self.yerr=self.ma1*0.01
        self.ax1.fill_between(self.time, self.ma1-self.yerr, self.ma1+self.yerr, alpha=0.5)
        self.ax1.plot(self.time, self.ma2, label=set2)
        self.ax1.fill_between(self.time, self.ma2-self.yerr, self.ma2+self.yerr, alpha=0.5)
        self.ax1.legend()
        self.ax1.margins(0)
        self.ax1.set_xlabel("time [s]")
        self.ax1.set_ylabel("power [W]")

        self.hor1 = self.percentile(0.5, self.cock)
        self.ver1 = self.percentile(0.5, self.mdiff)
        self.hor2 = self.percentile(0.9, self.cock)
        self.ver2 = self.percentile(0.9, self.mdiff)
        self.hor3 = self.percentile(0.95, self.cock)
        self.ver3 = self.percentile(0.95, self.mdiff)
        print(self.ver3)

        self.ax2.hist(self.mdiff, bins=self.bins, range=(0,self.maxerr), cumulative=True, histtype='step')
        ein = self.ax2.hlines(y=self.ver1,  xmin=0, xmax=self.hor1, colors='blue', label='50%')
        self.ax2.vlines(x=self.hor1,  ymin=0, ymax=self.ver1, colors='blue')
        zwei = self.ax2.hlines(y=self.ver2,  xmin=0, xmax=self.hor2, colors='orange', label='90%')
        self.ax2.vlines(x=self.hor2,  ymin=0, ymax=self.ver2, colors='orange')
        drei = self.ax2.hlines(y=self.ver3,  xmin=0, xmax=self.hor3, colors='pink', label='95%')
        self.ax2.vlines(x=self.hor3,  ymin=0, ymax=self.ver3, colors='pink')
        self.extraticks = (self.hor1, self.hor2, self.hor3)
        self.ax2.set_xticks(list(self.ax2.get_xticks()) + list(self.extraticks))
        self.ax2.legend((ein, zwei, drei), ('50%', '90%', '95%'), title='events percentile')
        self.ax2.margins(0)
        self.ax2.xaxis.set_minor_locator(AutoMinorLocator())
        self.ax2.set_xlabel("% discrepancy between power values")
        self.ax2.set_ylabel("# of time events")
    def dotProduct(self):
        f1=self.ma1
        f2=self.ma2
        #measure of similarity
        return np.sum(f1*f2)/np.sqrt(np.sum(f1**2)*np.sum(f2**2))

    def percentile(self, n, quantity): #n between [0,1]
        return (np.cumsum(quantity) < np.sum(quantity)*n).sum()

    def draw(self):
        return self.fig

    def clear(self):
        self.fig.close()

#commented out for later

# ax1.plot(time, ma1, label='lez')
# yerr=ma1*0.01
# ax1.fill_between(time, ma1-yerr, ma1+yerr, alpha=0.5)
# ax1.plot(time, ma2, label='tac')
# ax1.fill_between(time, ma2-yerr, ma2+yerr, alpha=0.5)
# ax1.legend()

# ax2.hist(mdiff, bins=bins, range=(0,maxerr), cumulative=True, histtype='step')
# ein = ax2.hlines(y=ver5,  xmin=0, xmax=hor5, colors='blue', label='50%')
# ax2.vlines(x=hor5,  ymin=0, ymax=ver5, colors='blue')
# zwei = ax2.hlines(y=ver9,  xmin=0, xmax=hor9, colors='orange', label='50%')
# ax2.vlines(x=hor9,  ymin=0, ymax=ver9, colors='orange')
# drei = ax2.hlines(y=ver95,  xmin=0, xmax=hor95, colors='magenta', label='50%')
# ax2.vlines(x=hor95,  ymin=0, ymax=ver95, colors='magenta')

# ax2.legend((ein, zwei, drei), ('50%', '90%', '95%'), title='events percentile')
# extraticks = (hor5, hor9, hor95)
# ax2.set_xticks(list(ax2.get_xticks()) + list(extraticks))

# ax2.margins(0)
# ax2.xaxis.set_minor_locator(AutoMinorLocator())

# ax2.set_xlabel("% discrepancy between values")
# ax2.set_ylabel("# of events")
# plt.get_current_fig_manager().window.showMaximized()
# plt.show()
