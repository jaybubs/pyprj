import numpy as np
class controller():
    def __init__(self, model):
        self.model = model

    def add(self, entity1, entity2):
        # self.x = np.append(self.x, self.entity)
        # self.y = np.append(self.y, self.entity)
        # return variable
        return self.model.addPoint(entity1, entity2)

    def hello(self):
        print("hi")
