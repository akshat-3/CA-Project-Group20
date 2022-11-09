from Router import * 
from port import *

class Mesh():
    def __init__(self):
        self.router_a= Router(0, 0)
        self.router_b= Router(0, 1)
        self.router_c= Router(1, 1)
        self.router_d= Router(1, 0)

        #self.routers = [self.router_a, self.router_b, self.router_c, self.router_d]

        self.router_a.neighbour_list = [self.router_b, self.router_d]
        self.router_b.neighbour_list = [self.router_a, self.router_c]
        self.router_c.neighbour_list = [self.router_b, self.router_d]
        self.router_d.neighbour_list = [self.router_a, self.router_c]



        port_ab= Port()
        self.router_a.east_input_port= port_ab
        self.router_b.west_output_port= port_ab
        port_ab.setPort(self.router_a, self.router_b)

        port_ba= Port()
        self.router_b.west_input_port= port_ba
        self.router_a.east_output_port= port_ba
        port_ab.setPort(self.router_b, self.router_a)

        port_bc= Port()
        self.router_b.south_input_port= port_bc
        self.router_c.north_output_port= port_bc
        port_bc.setPort(self.router_b, self.router_c)

        port_cb= Port()
        self.router_c.north_input_port= port_cb
        self.router_b.south_output_port= port_cb
        port_cb.setPort(self.router_c, self.router_b)

        port_cd= Port()
        self.router_c.west_input_port= port_cd
        self.router_d.east_output_port= port_cd
        port_cd.setPort(self.router_c, self.router_d)

        port_dc= Port()
        self.router_d.east_input_port= port_dc
        self.router_c.west_output_port= port_dc
        port_dc.setPort(self.router_d, self.router_c)

        port_da= Port()
        self.router_d.north_input_port= port_da
        self.router_a.south_output_port= port_da
        port_da.setPort(self.router_d, self.router_a)

        port_ad= Port()
        self.router_d.north_output_port= port_ad
        self.router_a.south_input_port= port_ad
        port_ad.setPort(self.router_a, self.router_d)

        self.router_a.ports_list = [port_ab, port_ad]
        self.router_b.ports_list = [port_ba, port_bc]
        self.router_c.ports_list = [port_cb, port_cd]
        self.router_d.ports_list = [port_da, port_dc]
    
    # def buff_check(self):
    #     if(self.router_a.pe_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_a.south_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_a.east_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_b.pe_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_b.west_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_b.south_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_c.pe_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_c.west_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_c.north_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_d.pe_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_d.north_buffer[0]!=["0"*34]):
    #         dummy()
    #     if(self.router_d.east_buffer[0]!=["0"*34]):
    #         dummy()

    # def dummy(self):
    #     return "Actions bhay router wale"

    def update(self,clock):
        self.router_a.update(clock)
        self.router_b.update(clock)
        self.router_c.update(clock)
        self.router_d.update(clock)
    
    def injectPacket(self, flit,count,source):
        if(source=='A'):
            self.router_a.pe_buffer[count] = flit
        elif(source=='B'):
            self.router_b.pe_buffer[count]=flit
        elif(source=='C'):
            self.router_c.pe_buffer[count]=flit
        elif(source=='D'):
            self.router_d.pe_buffer[count]=flit
        return 1


    def readInp(self, s):

        return "ehhe"