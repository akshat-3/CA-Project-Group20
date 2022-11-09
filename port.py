import Clock

class Port():
    def __init__(self):
        self.unused = 1
        self.input_edge = None
        self.output_edge = None
    
    def setPort(self, a, b):
        self.input_edge = a
        self.output_edge = b

