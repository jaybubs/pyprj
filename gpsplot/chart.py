# from sys import argv
#argv is stored as class list where 0th element is the script name
from scipy.signal import savgol_filter as SF

# numOfVars = len(argv)-1
# desiredY = input("y axis variable: ")
desiredY = 'watts'
desiredX = 'secs'

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
