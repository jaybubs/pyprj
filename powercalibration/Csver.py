#takes in csv, make sure the columns have headers
#csv treatment is down to the user
import pandas as p
from scipy.signal import savgol_filter as SF

class Csver():
    def __init__(self, filename):
        self._filename = filename
        self.__file = p.read_csv(self._filename)

    def column(self,header):
        return self.__file.loc[:,header]

    def movingAverage(self, header, period=5, polynomial=2):
        #default period 5, polynomial 2
        return SF(self.column(header), period, polynomial)
