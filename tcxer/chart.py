from sys import argv
#argv is stored as class list where 0th element is the script name
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.signal import savgol_filter as SF

numOfVars = len(argv)-1
# desiredY = input("y axis variable: ")
desiredY = 'watts'

def makeSoup(arg): #need to be fed argv
    with open(arg) as fp:
        return BS(fp, 'html.parser')

def createXAxis():
    for i in BS.find_all('time'):
        x += i.string.split('\n')
    return x

def createYAxis():
    for i in BS.find_all(str(desiredY)):
        yvals += i.string.split('\n')
        y = [float(y) for y in yvals]
    return y

def getMovingAverage(variable):
    return SF(variable, 21, 2)

####################execution

def createData(arguments):
    for i in arguments[1:]:
        x = createXAxis(makeSoup(i))
        y = createYAxis(makeSoup(i))
        MA = getMovingAverage(y)
        return x,y,MA

print(createData(argv))
####################plotting

# fig, (ax1, ax2) = plt.subplots(2,1)


####################old shit below
# x1 = []
# x2 = []
# y1 = []
# y2 = []

# with open('ramp.tcx') as file1:
#     soup1 = BS(file1, 'html.parser')

# with open('ramptest.tcx') as file2:
#     soup2 = BS(file2, 'html.parser')

# for i in soup1.find_all('time'):
#     x1 += i.string.split('\n') #use \n to parse string by line

# for i in soup2.find_all('time'):
#     x2 += i.string.split('\n')


# for i in soup1.find_all('watts'):
#     y1 += i.string.split('\n')
#     y1 = [float(y) for y in y1]

# y1MA = SF(y1, 21, 2)

# for i in soup2.find_all('watts'):
#     y2 += i.string.split('\n')
#     y2 = [float(y) for y in y2]

# y2MA = SF(y2, 21, 2)

# fig, (ax1, ax2) = plt.subplots(2,1)
# ax1.plot(x1, y1, label='4iii')
# ax1.plot(x2, y2, label='trainer')
# ax2.plot(x1[len(x1)-len(y1MA):],y1MA, label='4iii 21 sec MA poly 2')
# ax2.plot(x2[len(x2)-len(y2MA):],y2MA, label='trainer 21 sec MA poly 2')
# plt.yticks(np.arange(min(y1), max(y1)+1, 10.0))
# plt.yticks(np.arange(min(y2), max(y2)+1, 10.0))
# ax1.xaxis.set_major_locator(ticker.LinearLocator(5))
# ax2.xaxis.set_major_locator(ticker.LinearLocator(5))
# ax1.set_ylim(bottom=100)
# ax2.set_ylim(bottom=100)
# ax1.set_xlim(left=50)
# ax2.set_xlim(left=50)
# ax1.legend()
# ax2.legend()
# plt.show()
