from sys import argv
from Tcxer import Tcxer
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

file1 = Tcxer('swiss.tcx', 'time', 'watts')
file2 = Tcxer('swissclimb.tcx', 'time', 'watts')

file1.makeSoup()
file1.findAll()
file1.movingAverage(21,2)
file2.makeSoup()
file2.findAll()
file2.movingAverage(21,2)


fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(file1._valx, file1._valy, label='4iii')
ax1.plot(file2._valx, file2._valy, label='trainer')
ax2.plot(file1._valx[len(file1._valx)-len(file1._movAv):], file1._movAv, label='4iii 21 sec MA poly 2')
ax2.plot(file2._valx[len(file2._valx)-len(file2._movAv):], file2._movAv, label='trainer 21 sec MA poly 2')
# plt.yticks(np.arange(min( file1._valy), max( file1._valy)+1, 10.0))
# plt.yticks(np.arange(min( file2._valy), max( file2._valy)+1, 10.0))
ax1.xaxis.set_major_locator(ticker.LinearLocator(5))
ax2.xaxis.set_major_locator(ticker.LinearLocator(5))
ax1.set_ylim(bottom=100)
ax2.set_ylim(bottom=100)
ax1.set_xlim(left=50)
ax2.set_xlim(left=50)
ax1.legend()
ax2.legend()
plt.show()
