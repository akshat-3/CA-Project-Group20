from Router import *
from Mesh import *

class CrossBar:
    """0,0 : A
       0,1 : B
       1,1 : C
       1,0 : D"""
    def __init__(self):
        # self.northI = northI
        # self.southI = southI
        # self.westI = westI
        # self.eastI = eastI
        # self.northO = northO
        # self.southO = southO
        # self.westO = westO
        # self.eastO = eastO
        self.currentConnected = []

    def makeconnection(self,dest_router,master,slave,direction):
        print("Making connection")
        #print(dest_router.XCurrent,dest_router.YCurrent)
        if self.moveData(dest_router,direction):
            self.currentConnected.append([dest_router,master,slave,direction])
    
    def sendFlit(self, master, flit):
        for i in self.currentConnected:
            if i[1] == master:
                if(i[3] == "NORTH"):
                    i[0].buffer_shuffle(i[3])
                    i[0].north_buffer[0] = flit
                if(i[3] == "EAST"):
                    i[0].buffer_shuffle(i[3])
                    i[0].east_buffer[0] = flit
                if(i[3] == "WEST"):
                    i[0].buffer_shuffle(i[3])
                    i[0].west_buffer[0] = flit
                    print(i[0].west_buffer)
                if(i[3] == "SOUTH"):
                    i[0].buffer_shuffle(i[3])
                    i[0].south_buffer[0] = flit


    def deleteConnection(self, master):
        for i in self.currentConnected:
            if i[1] == master:
                self.currentConnected.remove(i)

    def checkNext(self, next, dir):
        if(next == None):
            pass
        #if next is empty so data is shifted
        else:
            if(dir == "NORTH"):
                if(next.isempty_north_buffer()):
                    print('hello')
                    return True
            if(dir == "EAST"):
                if(next.isempty_east_buffer()):
                    return True
            if(dir == "WEST"):
                if(next.isempty_west_buffer()):
                    return True
            if(dir == "SOUTH"):
                if(next.isempty_south_buffer()):
                    return True
        return False

    def moveData(self,dest,dir):
        if self.checkNext(dest,dir):
            return True 