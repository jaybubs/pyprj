from sys import argv
from Tcxer import Tcxer
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

files = []
for argument in argv[1:]: #[1:] because the 0th element is the script name
    files.append(argument) # instead of += need append because += will decompose the filename into individual letters

data = []
fig, (ax1, ax2) = plt.subplots(2,1) #ax1 for 1sec ax2 for MA
for filename in files:
    file = Tcxer(filename, 'time', 'watts')
    file.makeSoup() #parses xml
    file.findAll() #creates a couple of lists that can be accessed by _val
    file.movingAverage(21,2) #creates a list that can be accessed by _movAv
    data.append(file._valx)
    data.append(file._valy)
    data.append(file._movAv)
    ax1.plot(file._valx, file._valy, label=filename)
    ax2.plot(file._valx[len(file._valx)-len(file._movAv):], file._movAv, label=filename+' 21 sec MA poly 2')
    
# datanp = np.array(data) #creates an array of lists (lists not guaranteed to have the same dimension)

# ax1.plot(file1._valx, file1._valy, label='4iii')
# ax1.plot(file2._valx, file2._valy, label='trainer')
# ax2.plot(file1._valx[len(file1._valx)-len(file1._movAv):], file1._movAv, label='4iii 21 sec MA poly 2')
# ax2.plot(file2._valx[len(file2._valx)-len(file2._movAv):], file2._movAv, label='trainer 21 sec MA poly 2')
# plt.yticks(np.arange(min( file1._valy), max( file1._valy)+1, 10.0))
# plt.yticks(np.arange(min( file2._valy), max( file2._valy)+1, 10.0))
ax1.xaxis.set_major_locator(ticker.LinearLocator(5))
ax2.xaxis.set_major_locator(ticker.LinearLocator(5))
ax1.set_ylim(bottom=0)
ax2.set_ylim(bottom=0)
ax1.set_xlim(left=0)
ax2.set_xlim(left=0)
ax1.legend()
ax2.legend()
plt.show()
