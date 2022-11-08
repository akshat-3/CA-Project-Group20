
class Clock():
    def __init__(self):
        self.count = 0
        self.value = 0
    
    def startClock(self):  
        self.value = 1
        self.count = 1
    
    def updateCycle(self):
        self.value = 0
        self.value = 1
        self.count += 1
       
    def stopClock(self):
        self.count = 0
        self.value = 0
        