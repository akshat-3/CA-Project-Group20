import numpy as np
import port as port

class Router():
    # 5 ports (input and output)
    # Class Ports
    # input connected Output Connected
    # processing element dummy class
    # class crossbar (connects input and output port)

    def __init__(self):
        self.XCurrent = 0
        self.YCurrent = 0
        self.ports = port()        
        elfr)f.buffernp.=np.empty(5, dtype=string)
    
    def XYrouting(self,Xdest,Ydest):
        Xoffset = Xdest-self.XCurrent
        Yoffset = Ydest-self.YCurrent
        if Xoffset<0:
            self.XCurrent -= 1
        if Xoffset>0:
            self.XCurrent += 1
        if Xoffset==0 and Yoffset<0:
            self.YCurrent += 1
        if Xoffset==0 and Yoffset>0:
            self.YCurrent -= 1

    def ifchannel(self, Xoff, Yoff):
        if Xoff==0 and Yoff==0:
            self.channel = "idk" #internal