class Packet():
    def __init__(self,Payload,Source,Destination,InjectCycleNum):
        self.Payload = Payload
        self.Source = Source
        self.dict = {"A":"00","B":"01","C":"11","D":"10"}
        self.Destination = Destination
        self.InjectCycleNum = InjectCycleNum

    def header(self):
        return "0"*28 + self.dict[self.Destination] + self.dict[self.Source] + "00"

    def tail(self):
        return "0"*32+ "10"

    def body(self):
        return [self.Payload[0:32]+"01",self.Payload[32:64]+"01",self.Payload[64:96]+"01"]
    
    def flit(self):
        return [self.header()]+self.body()+[self.tail()]
    