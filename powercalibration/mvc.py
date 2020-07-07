#php-like generic mvc with some action pseudocode
class Model():
    def __init__(self):
        self.text = "hello"

class View():
    def __init__(self, model):
        self.model = model

    def output():
        print(self.model.text)

class Controller():
    def __init__(self, model):
        self.model = model

    def press():
        self.model.text = "new text"

model = Model()
#controller and view must share the model
controller = Controller(model)
view = View(model)
if(button=pressed):
    controller.press()
echo view.output
