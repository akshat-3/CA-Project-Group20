from port import *
from crossbar import *
import Processing_element

class Router():
    # 5 ports (input and output)
    # Class Ports
    # input connected Output Connected
    # processing element dummy class
    # class crossbar (connects input and output port)

    def __init__(self,X,Y):
        
        self.XCurrent = X
        self.YCurrent = Y
        self.crossbar = CrossBar()
        self.pe= Processing_element.pe()

        self.north_input_port = None
        self.south_input_port = None    
        self.east_input_port = None    
        self.west_input_port = None    
        self.pe_input_port = None

        self.north_output_port = None    
        self.south_output_port = None    
        self.east_output_port = None    
        self.west_output_port = None    
        self.pe_output_port = None  

        self.north_buffer=["0"*34]*5
        self.south_buffer=["0"*34]*5
        self.east_buffer=["0"*34]*5
        self.west_buffer=["0"*34]*5
        self.pe_buffer=["0"*34]*5

        self.neighbour_list = []

        port_pr= Port()
        self.pe.input_port= port_pr
        self.pe_output_port= port_pr
        port_pr.setPort(self.pe.input_port, self.pe_output_port)

        port_rp= Port()
        self.pe_input_port= port_rp
        self.pe.output_port= port_rp
        port_rp.setPort(self.pe_input_port, self.pe.input_port)

    def switchAllocator(self,Xdest,Ydest):
        Xoffset = Xdest-self.XCurrent
        Yoffset = Ydest-self.YCurrent
        if Xoffset<0:
            return self.XCurrent - 1,self.YCurrent
        if Xoffset>0:
            return self.XCurrent + 1,self.YCurrent
        if Xoffset==0 and Yoffset<0:
            return self.YCurrent + 1,self.XCurrent
        if Xoffset==0 and Yoffset>0:
            return self.YCurrent - 1,self.XCurrent

    def ifchannel(self, Xoff, Yoff):
        if Xoff==0 and Yoff==0:
            self.channel = "idk" #internal
    
    def isempty_north_buffer(self):
        for i in self.north_buffer:
            if i == '0'*34:
                return True
        return False
    
    def isempty_south_buffer(self):
        for i in self.south_buffer:
            if i == '0'*34:
                return True
        return False

    def isempty_east_buffer(self):
        for i in self.east_buffer:
            if i == '0'*34:
                return True
        return False
    
    def isempty_west_buffer(self):
        for i in self.west_buffer:
            if i == '0'*34:
                return True
        return False
    
    def checker(self,router,dir):
        if(dir=="NORTH"):
            return router.isempty_north_buffer()
        elif(dir=="SOUTH"):
            return router.isempty_south_buffer()
        elif(dir=="EAST"):
            return router.isempty_east_buffer()
        elif(dir=="WEST"):
            return router.isempty_west_buffer()

    def shiftNBuffer(self):
        for i in range(0,4):
            self.north_buffer[i] = self.north_buffer[i+1]

        self.north_buffer[4] = "0"*34

    def shiftSBuffer(self):
        for i in range(0,4):
            self.south_buffer[i] = self.south_buffer[i+1]

        self.south_buffer[4] = "0"*34
    
    def shiftEBuffer(self):
        for i in range(0,4):
            self.east_buffer[i] = self.east_buffer[i+1]

        self.east_buffer[4] = "0"*34
    
    def shiftWBuffer(self):
        for i in range(0,4):
            self.west_buffer[i] = self.west_buffer[i+1]

        self.west_buffer[4] = "0"*34

#add suport for other router
    def updateRouter(self):
        if self.north_buffer[0] != "0"*34:
            if(self.north_buffer[0][32:] == "00"):
                moveX,moveY = self.switchAllocator(self.north_buffer[0][28:30][0], self.north_buffer[0][28:30][1])
                if(moveX == self.XCurrent - 1):
                    self.crossbar.makeconnection(self.north_input_port,self.west_output_port,"EAST")
                elif(moveX == self.XCurrent + 1):
                    self.crossbar.makeconnection(self.north_input_port,self.east_output_port,"WEST")
                elif(moveY == self.YCurrent - 1):
                    self.crossbar.makeconnection(self.north_input_port,self.south_output_port,"NORTH")
                elif(moveY == self.YCurrent + 1):
                    self.crossbar.makeconnection(self.north_input_port,self.north_output_port,"SOUTH")
    
                self.crossbar.sendFlit(self.north_input_port,self.north_buffer[0])
                self.shiftNBuffer()
                
            elif(self.north_buffer[0][32:] == "01"):
                self.crossbar.sendFlit(self.north_input_port,self.north_buffer[0])
                self.shiftNBuffer()

            elif(self.north_buffer[0][32:] == "10"):
                self.crossbar.sendFlit(self.north_input_port,self.north_buffer[0])
                self.shiftNBuffer()
                self.crossbar.deleteConnection(self.north_input_port)
    
       