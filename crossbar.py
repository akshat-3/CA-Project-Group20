class CrossBar:
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

    def makeconnection(self,master,slave,direction):
        self.currentConnected.append(master,slave,direction)
    
    def sendFlit(self, master, flit):
        for i in self.currentConnected:
            if i[0] == master:
                if i[2] == "NORTH":
                    i[1].north_input_buffer[0] = flit
                elif i[2] == "SOUTH":
                    i[1].south_input_buffer[0] = flit
                elif i[2] == "EAST":
                    i[1].east_input_buffer[0] = flit
                elif i[2] == "WEST":
                    i[1].west_input_buffer[0] = flit

    def deleteConnection(self, master):
        for i in self.currentConnected:
            if i[0] == master:
                self.currentConnected.remove(i)
            
    

        
