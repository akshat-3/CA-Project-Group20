import logging

logging.basicConfig(filename="Logfile.log",filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Sending:
    def __init__(self, Router, buffer, direction,flag):
        #print('helo')
        self.count = 0
        self.buffer = buffer
        self.router = Router
        self.router_send = None
        self.dict = {'00':'A','01':'B','11':'C','10':'D'}
        self.directions = direction
        self.calculateReceiver(flag)
        

    def calculateReceiver(self,flag):
        #print('bufer',self.buffer)
        if self.router.XCurrent == int(self.buffer[0][28]) and self.router.YCurrent == int(self.buffer[0][29]):
            #print("halo\n")
            #print(self.router.XCurrent, self.router.YCurrent, self.router.north_buffer, self.router.south_buffer, self.router.east_buffer, self.router.west_buffer)
            if(self.router != None):
                if(self.directions == "NORTH"):
                    self.router.north_buffer = ["0"*34]*5
                elif(self.directions == "WEST"):
                    self.router.west_buffer = ["0"*34]*5
                elif(self.directions == "SOUTH"):
                    self.router.south_buffer = ["0"*34]*5
                elif(self.directions == "EAST"):
                    self.router.east_buffer = ["0"*34]*5
                elif(self.directions == "PE"):
                    self.router.pe_buffer = ["0"*34]*5
            
        else:
            moveX,moveY = self.router.switchAllocator(self.buffer[0][28],self.buffer[0][29], flag)
            if(self.router.neighbour_list[0].XCurrent == moveX and self.router.neighbour_list[0].YCurrent == moveY):
                self.router_send = self.router.neighbour_list[0]
            if(self.router.neighbour_list[1].XCurrent == moveX and self.router.neighbour_list[1].YCurrent == moveY):
                self.router_send = self.router.neighbour_list[1]
            #print('yo',moveX,moveY)
            if(moveX == self.router.XCurrent - 1):
                self.direction = "SOUTH"
            elif(moveX == self.router.XCurrent + 1):
                self.direction = "NORTH"
            elif(moveY == self.router.YCurrent - 1):
                self.direction = "EAST"
            elif(moveY == self.router.YCurrent + 1):
                self.direction = "WEST"

    
    def get_coord(self):
        return(self.x, self.y)

    def send(self,clock):
        if(self.router_send != None):
            route = self.dict[str(self.router_send.XCurrent)+str(self.router_send.YCurrent)]
            route_self = self.dict[str(self.router.XCurrent)+str(self.router.YCurrent)]
            logger.info('Router: ' + route + " Received from " +route_self+ " at clock cycle: "+ str(clock) +  ' Flit received: '+ self.buffer[self.count])
            if(self.direction == "NORTH"):
                self.router_send.north_buffer[self.count] = self.buffer[self.count]
                #print(self.router_send.north_buffer[self.count])
            elif(self.direction == "WEST"):
                self.router_send.west_buffer[self.count] = self.buffer[self.count]
                #print('west',self.router_send.west_buffer[self.count])
            elif(self.direction == "SOUTH"):
                self.router_send.south_buffer[self.count] = self.buffer[self.count]
                #print(self.router_send.south_buffer[self.count])
            elif(self.direction == "EAST"):
                self.router_send.east_buffer[self.count] = self.buffer[self.count]
                #print(self.router_send.east_buffer[self.count])
        self.count+=1
                
            