import numpy as np
import pandas as p
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

df = p.read_csv('stelvio.csv')
timeAxis = df.loc[:,'secs']
altAxis = df.loc[:,'alt']
distAxis = df.loc[:,'km']
lonAxis = df.loc[:,'lon']
latAxis = df.loc[:,'lat']
hrAxis = df.loc[:,'hr']
powerAxis = df.loc[:,'watts']
zeroAxis = np.zeros(len(timeAxis))

palette = ['royalblue', 'deepskyblue', 'lime', 'gold', 'darkorange', 'tomato', 'magenta']
hrZones = [139, 155, 162, 173, 178, 183, 200]
ftp=220
relPowerZones = [.55,.75,.90,1.05,1.2,1.5,50]
calcPowerZones = np.trunc([i * ftp for i in relPowerZones])
PZ=[121,165,198,231,264,330,5000]
fig, (ax1, ax2) = plt.subplots(2,1) #ax1 for HR ax2 for P

# plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot3D(lonAxis, latAxis, altAxis)

ax1.plot(distAxis, altAxis)
for i in range (len(hrZones)):
    ax1.fill_between(distAxis, altAxis, where=hrAxis <=hrZones[i], facecolor=palette[i], interpolate=False, zorder=len(hrZones)-i, label=hrZones[i])

ax1.legend()

ax2.plot(distAxis, altAxis)
for i in range (len(calcPowerZones)):
    ax2.fill_between(distAxis, altAxis, where=powerAxis <=calcPowerZones[i], facecolor=palette[i], interpolate=False, zorder=len(calcPowerZones)-i, label=calcPowerZones[i])

ax2.legend()

plt.show()
