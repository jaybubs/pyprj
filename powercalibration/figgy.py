#dummy example object for figures to be used by guis

class figgy():

    def __init__(self,x,y):
        self.fig = Figure(figsize=(5,4), dpi=100)
        self.x = x
        self.y = y
        
    def add(self, cord):
        self.fig.add_subplot(cord).plot(self.x, self.y)

    def draw(self):
        return self.fig
