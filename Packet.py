class Packet():
    def __init__(self,Payload,Source,Destination,InjectCycleNum):
        self.Payload = Payload
        self.Source = Source
        self.Destination = Destination
        self.InjectCycleNum = InjectCycleNum

        