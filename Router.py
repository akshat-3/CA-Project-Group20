from port import *
from crossbar import *
import Processing_element
from Sending import *

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
        self.send_flag = 0

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

        port_pr= Port()
        self.pe.input_port= port_pr
        self.pe_output_port= port_pr
        port_pr.setPort(self.pe.input_port, self.pe_output_port)

        port_rp= Port()
        self.pe_input_port= port_rp
        self.pe.output_port= port_rp
        port_rp.setPort(self.pe_input_port, self.pe.input_port)
        self.neighbour_list = []
        self.ports_list = []


    def switchAllocator(self,Xdest,Ydest):
        Xoffset = int(Xdest)-self.XCurrent
        Yoffset = int(Ydest)-self.YCurrent
        if Xoffset<0:
            return self.XCurrent - 1,self.YCurrent
        if Xoffset>0:
            return self.XCurrent + 1,self.YCurrent
        if Xoffset==0 and Yoffset<0:
            return self.XCurrent, self.YCurrent - 1
        if Xoffset==0 and Yoffset>0:
            return self.XCurrent, self.YCurrent + 1

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
    
    def isempty_pe_buffer(self):
        for i in self.pe_buffer:
            if i == '0'*34:
                return True
        return False
    
    # def checker(self,router,dir):
    #     if(dir=="NORTH"):
    #         return router.isempty_north_buffer()
    #     elif(dir=="SOUTH"):
    #         return router.isempty_south_buffer()
    #     elif(dir=="EAST"):
    #         return router.isempty_east_buffer()
    #     elif(dir=="WEST"):
    #         return router.isempty_west_buffer()

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
    
    def shiftPEBuffer(self):
        for i in range(0,4):
            self.pe_buffer[i] = self.pe_buffer[i+1]

        self.pe_buffer[4] = "0"*34

    def buffer_shuffle(self, dir):
        if(dir=="NORTH"):
            for i in range(0,5):
                if(self.north_buffer[i]=="0"*34):
                    return i
        elif(dir=="SOUTH"):
            for i in range(0,5):
                if(self.south_buffer[i]=="0"*34):
                    return i
        elif(dir=="EAST"):
            for i in range(0,5):
                if(self.east_buffer[i]=="0"*34):
                    return i
        elif(dir=="WEST"):
            for i in range(0,5):
                if(self.west_buffer[i]=="0"*34):
                    return i
        elif(dir=="PE"):
            for i in range(0,5):
                if(self.pe_buffer[i]=="0"*34):
                    return i
    def update(self):
        if self.send_flag==1:
            self.send.send()
            if(self.send.count==5):
                self.send_flag= 0
            pass
        elif self.isempty_pe_buffer()==False:
            print('1')
            self.send= Sending(self, self.pe_buffer)
            self.pe_buffer= ["0"*34]*5
            self.send_flag= 1
        elif self.isempty_west_buffer()==False:
            print('2')
            self.send= Sending(self, self.west_buffer)
            self.west_buffer= ["0"*34]*5
            self.send_flag= 1
        elif self.isempty_north_buffer()==False:
            print('3')
            self.send= Sending(self, self.north_buffer)
            self.north_buffer= ["0"*34]*5
            self.send_flag= 1
        elif self.isempty_east_buffer()==False:
            print('4')
            self.send= Sending(self, self.east_buffer)
            self.east_buffer= ["0"*34]*5
            self.send_flag= 1
        elif self.isempty_south_buffer()==False:
            print('5')
            self.send= Sending(self, self.south_buffer)
            self.south_buffer= ["0"*34]*5
            self.send_flag= 1
        
        # if self.isempty_pe_buffer()==True:
        #     self.startRouting('PE')
        # if self.isempty_east_buffer() == False:
        #     self.startRouting('EAST')
        # if self.isempty_north_buffer() == False:
        #     self.startRouting('NORTH')
        # if self.isempty_south_buffer() == False:
        #     self.startRouting('SOUTH')

        # self.startRouting('WEST')
        
        # if self.isempty_pe_buffer() == False:
        #     self.startRouting('PE')

    def startRouting(self,dir):
           
        if(dir == 'NORTH'):
            if(self.north_buffer[0][32:] == '0'*2):
                moveX,moveY = self.switchAllocator(self.north_buffer[0][28:30][0], self.north_buffer[0][28:30][1])
                router_send = None
                if(self.neighbour_list[0].XCurrent == moveX and self.neighbour_list[0].YCurrent == moveY):
                    router_send = self.neighbour_list[0]
                if(self.neighbour_list[1].XCurrent == moveX and self.neighbour_list[1].YCurrent == moveY):
                    router_send = self.neighbour_list[1]
                if(moveX == self.XCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.north_input_port,self.north_output_port,"SOUTH")
                elif(moveX == self.XCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.north_input_port,self.south_output_port,"NORTH")
                elif(moveY == self.YCurrent - 1):
                    self.crossbar.makeconnection(router_send.self.north_input_port,self.west_output_port,"EAST")
                elif(moveY == self.YCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.north_input_port,self.east_output_port,"WEST")
                self.crossbar.sendFlit(self.north_input_port,self.north_buffer[0])
                self.shiftNBuffer()
            
            if(self.north_buffer[0][32:] == '01'):
                self.crossbar.sendFlit(self.north_input_port,self.north_buffer[0])
                self.shiftNBuffer()
            
            if(self.north_buffer[0][32:] == '10'):
                self.crossbar.sendFlit(self.north_input_port,self.north_buffer[0])
                self.shiftNBuffer()
                self.crossbar.deleteConnection(self.north_input_port)
        
        if(dir == 'PE'):
            if(self.pe_buffer[0][32:] == '0'*2):
                moveX,moveY = self.switchAllocator(self.pe_buffer[0][28:30][0], self.pe_buffer[0][28:30][1])
                router_send = None
                if(self.neighbour_list[0].XCurrent == moveX and self.neighbour_list[0].YCurrent == moveY):
                    router_send = self.neighbour_list[0]
                if(self.neighbour_list[1].XCurrent == moveX and self.neighbour_list[1].YCurrent == moveY):
                    router_send = self.neighbour_list[1]
                if(moveX == self.XCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.pe_input_port,self.north_output_port,"SOUTH")
                elif(moveX == self.XCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.pe_input_port,self.south_output_port,"NORTH")
                elif(moveY == self.YCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.pe_input_port,self.west_output_port,"EAST")
                elif(moveY == self.YCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.pe_input_port,self.east_output_port,"WEST")
                self.crossbar.sendFlit(self.pe_input_port,self.pe_buffer[0])
                self.shiftPEBuffer()
            
            if(self.pe_buffer[0][32:] == '01'):
                self.crossbar.sendFlit(self.pe_input_port,self.pe_buffer[0])
                self.shiftPEBuffer()

            
            if(self.pe_buffer[0][32:] == '10'):
                self.crossbar.sendFlit(self.pe_input_port,self.pe_buffer[0])
                self.shiftPEBuffer()
                self.crossbar.deleteConnection(self.pe_input_port)

        if(dir == 'SOUTH'):
            if(self.south_buffer[0][32:] == '0'*2):
                moveX,moveY = self.switchAllocator(self.south_buffer[0][28:30][0], self.south_buffer[0][28:30][1])
                router_send = None
                if(self.neighbour_list[0].XCurrent == moveX and self.neighbour_list[0].YCurrent == moveY):
                    router_send = self.neighbour_list[0]
                if(self.neighbour_list[1].XCurrent == moveX and self.neighbour_list[1].YCurrent == moveY):
                    router_send = self.neighbour_list[1]
                if(moveX == self.XCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.south_input_port,self.north_output_port,"SOUTH")
                elif(moveX == self.XCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.south_input_port,self.south_output_port,"NORTH")
                elif(moveY == self.YCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.south_input_port,self.west_output_port,"EAST")
                elif(moveY == self.YCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.south_input_port,self.east_output_port,"WEST")
                self.crossbar.sendFlit(self.south_input_port,self.south_buffer[0])
                self.shiftSBuffer()
            
            if(self.south_buffer[0][32:] == '01'):
                self.crossbar.sendFlit(self.south_input_port,self.south_buffer[0])
                self.shiftSBuffer()
            
            if(self.south_buffer[0][32:] == '10'):
                self.crossbar.sendFlit(self.south_input_port,self.south_buffer[0])
                self.shiftSBuffer()
                self.crossbar.deleteConnection(self.south_input_port)
        
        if(dir == 'EAST'):
            if(self.east_buffer[0][32:] == '0'*2):
                moveX,moveY = self.switchAllocator(self.east_buffer[0][28:30][0], self.east_buffer[0][28:30][1])
                router_send = None
                if(self.neighbour_list[0].XCurrent == moveX and self.neighbour_list[0].YCurrent == moveY):
                    router_send = self.neighbour_list[0]
                if(self.neighbour_list[1].XCurrent == moveX and self.neighbour_list[1].YCurrent == moveY):
                    router_send = self.neighbour_list[1]
                if(moveX == self.XCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.east_input_port,self.north_output_port,"SOUTH")
                elif(moveX == self.XCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.east_input_port,self.south_output_port,"NORTH")
                elif(moveY == self.YCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.east_input_port,self.west_output_port,"EAST")
                elif(moveY == self.YCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.east_input_port,self.east_output_port,"WEST")
                self.crossbar.sendFlit(self.east_input_port,self.east_buffer[0])
                self.shiftEBuffer()
            
            if(self.east_buffer[0][32:] == '01'):
                self.crossbar.sendFlit(self.east_input_port,self.east_buffer[0])
                self.shiftEBuffer()
            
            if(self.east_buffer[0][32:] == '10'):
                self.crossbar.sendFlit(self.east_input_port,self.east_buffer[0])
                self.shiftEBuffer()
                self.crossbar.deleteConnection(self.east_input_port)
        
        if(dir == 'WEST'):
            if(self.west_buffer[0][32:] == '0'*2):
                moveX,moveY = self.switchAllocator(self.west_buffer[0][28:30][0], self.west_buffer[0][28:30][1])
                router_send = None
                if(self.neighbour_list[0].XCurrent == moveX and self.neighbour_list[0].YCurrent == moveY):
                    router_send = self.neighbour_list[0]
                if(self.neighbour_list[1].XCurrent == moveX and self.neighbour_list[1].YCurrent == moveY):
                    router_send = self.neighbour_list[1]
                if(moveX == self.XCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.west_input_port,self.north_output_port,"SOUTH")
                elif(moveX == self.XCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.west_input_port,self.south_output_port,"NORTH")
                elif(moveY == self.YCurrent - 1):
                    self.crossbar.makeconnection(router_send,self.west_input_port,self.west_output_port,"EAST")
                elif(moveY == self.YCurrent + 1):
                    self.crossbar.makeconnection(router_send,self.west_input_port,self.east_output_port,"WEST")
                self.crossbar.sendFlit(self.west_input_port,self.west_buffer[0])
                self.shiftWBuffer()
            
            if(self.west_buffer[0][32:] == '01'):
                self.crossbar.sendFlit(self.west_input_port,self.west_buffer[0])
                self.shiftWBuffer()
            
            if(self.west_buffer[0][32:] == '10'):
                self.crossbar.sendFlit(self.west_input_port,self.west_buffer[0])
                self.shiftWBuffer()
                self.crossbar.deleteConnection(self.west_input_port)