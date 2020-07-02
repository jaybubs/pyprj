from sys import argv
import numpy as np
from Csver import Csver
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import matplotlib.gridspec as gridspec
from matplotlib.ticker import AutoMinorLocator


def dotProduct(f1,f2):
    #measure of similarity
    return np.sum(f1*f2)/np.sqrt(np.sum(f1**2)*np.sum(f2**2))

def percentile(n, quantity): #n between [0,1]
    return (np.cumsum(quantity) < np.sum(quantity)*n).sum()

set1 = Csver('lezynehardknott.csv')
set2 = Csver('tacxhardknott.csv')
time = set1.column('secs')
ma1 = set1.movingAverage('watts')
ma2 = set2.movingAverage('watts')
print(dotProduct(ma1,ma2))
mdiff = np.absolute(ma1-ma2)*100/((ma1+ma2)/2.0)


# files = [] #to supply csvs
# for argument in argv[1:]:
#     files.append(argument)

#commented out for later
error = 1 #percentage error in equipment, both crank and trainer have 1% in this case
bins = 50
maxerr = np.max(mdiff)
cock, balls = np.histogram(mdiff, bins=bins, range=(0,maxerr))

hor5 = percentile(0.5, cock)
ver5 = percentile(0.5, mdiff)
hor9 = percentile(0.9, cock)
ver9 = percentile(0.9, mdiff)
hor95 = percentile(0.95, cock)
ver95 = percentile(0.95, mdiff)

plt.figure()
# fig, (ax1, ax2) = plt.subplots(2,1) #ax1 for HR ax2 for P
gs = gridspec.GridSpec(2,1, height_ratios=[1,1])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])

ax1.plot(time, ma1, label='lez')
# ax1.errorbar(time, ma1, yerr=ma1*(error/100.), color='black', barsabove='False')
yerr=ma1*0.01
ax1.fill_between(time, ma1-yerr, ma1+yerr, alpha=0.5)
ax1.plot(time, ma2, label='tac')
ax1.fill_between(time, ma2-yerr, ma2+yerr, alpha=0.5)
ax1.legend()

ax2.hist(mdiff, bins=bins, range=(0,maxerr), cumulative=True, histtype='step')
ein = ax2.hlines(y=ver5,  xmin=0, xmax=hor5, colors='blue', label='50%')
ax2.vlines(x=hor5,  ymin=0, ymax=ver5, colors='blue')
zwei = ax2.hlines(y=ver9,  xmin=0, xmax=hor9, colors='orange', label='50%')
ax2.vlines(x=hor9,  ymin=0, ymax=ver9, colors='orange')
drei = ax2.hlines(y=ver95,  xmin=0, xmax=hor95, colors='magenta', label='50%')
ax2.vlines(x=hor95,  ymin=0, ymax=ver95, colors='magenta')

ax2.legend((ein, zwei, drei), ('50%', '90%', '95%'), title='events percentile')
extraticks = (hor5, hor9, hor95)
ax2.set_xticks(list(ax2.get_xticks()) + list(extraticks))

# trans = transforms.blended_transform_factory(
#         ax2.get_xticklabels()[0].get_transform(), ax2.transData)

# ax2.text(hor5,ver5, "{:.0f}".format(hor5), #{:.0f} float to 2 dec places
#         color="red", transform=trans, ha="right", va="center")
ax2.margins(0)
ax2.xaxis.set_minor_locator(AutoMinorLocator())

ax2.set_xlabel("% discrepancy between values")
ax2.set_ylabel("# of events")
plt.get_current_fig_manager().window.showMaximized()
plt.show()
