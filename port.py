class Port():
    def __init__(self, a, b):
        self.flag = 0
        self.end_1 = a
        self.end_2 = b

    def sender_switch(self):
        self.flag+= 1
        self.flag= self.flag%2