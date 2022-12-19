class Packet():
    def __init__(self,Payload,Source,Destination,InjectCycleNum,PacketNum):
        self.Payload = Payload
        self.Source = Source
        self.dict = {"A":"00","B":"01","C":"11","D":"10"}
        self.Destination = Destination
        self.InjectCycleNum = InjectCycleNum
        self.PacketNum = PacketNum

    def header(self):
        data  = str(bin(self.PacketNum)[2:])
        length = 28 - len(data)
        return "0"*length + data + self.dict[self.Destination] + self.dict[self.Source] + "00"

    def tail(self):
        data  = str(bin(self.PacketNum)[2:])
        length = 28 - len(data)
        return "0"*length + data +"000011"

    def body(self):
        return [self.Payload[0:32]+"01",self.Payload[32:64]+"01",self.Payload[64:96]+"01"]
    
    def flit(self):
        # print(self.PacketNum)
        # print(self.header()) 
        # print(self.tail())
        return [self.header()]+self.body()+[self.tail()]

    