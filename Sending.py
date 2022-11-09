
class Sending:
    def __init__(self, Router, buffer):
        print('helo')
        self.count = 0
        self.buffer = buffer
        self.router = Router
        self.router_send = None
        self.calculateReceiver()

    def calculateReceiver(self):
        #print('bufer',self.buffer)
        if self.router.XCurrent == int(self.buffer[0][28]) and self.router.YCurrent == int(self.buffer[0][29]):
            print(self.router.XCurrent, self.router.YCurrent, self.router.north_buffer, self.router.south_buffer, self.router.east_buffer, self.router.west_buffer)
        else:
            moveX,moveY = self.router.switchAllocator(self.buffer[0][28],self.buffer[0][29])
            if(self.router.neighbour_list[0].XCurrent == moveX and self.router.neighbour_list[0].YCurrent == moveY):
                self.router_send = self.router.neighbour_list[0]
            if(self.router.neighbour_list[1].XCurrent == moveX and self.router.neighbour_list[1].YCurrent == moveY):
                self.router_send = self.router.neighbour_list[1]
        #print(moveX,moveY)
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

    def send(self):
        #print(self.count)
        if(self.router_send != None):
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
                
            