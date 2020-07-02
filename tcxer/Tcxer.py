from bs4 import BeautifulSoup as BS
from scipy.signal import savgol_filter as SF
class Tcxer():

    #pulls desired values out of selected tags of input xml file, eg 'time' and 'watts' tag out of an tcx file

    def __init__(self, name, tagx, tagy):
        #constructor, only needs name
        self._name = name
        self._tagx = tagx
        self._tagy = tagy

        self._soup = None
        self._valx = None
        self._valy = None
        self._movAv = None
        

    def makeSoup(self):
        #this method parses the xml file and makes it available for BS
        with open(self._name) as fp:
            self._soup = BS(fp, 'html.parser') 

    def findAll(self):
        #finds and returns all values for desired tags
        self._valx = []
        self._valy = []
        for value in self._soup.find_all(self._tagx):
            self._valx += value.string.split('\n')
        for value in self._soup.find_all(self._tagy):
            self._valy += value.string.split('\n')
            self._valy = [float(value) for value in self._valy]
        return self._valx, self._valy

    def movingAverage(self, period, polynomial):
        self._movAv = SF(self._valy, period, polynomial)
