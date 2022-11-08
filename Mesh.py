from Router import * 
import port

class Mesh():
    def __init__(self):
        router_a= Router(0, 0)
        router_b= Router(1, 0)
        router_c= Router(1, 1)
        router_d= Router(0, 1)

        port_ab= port()
        router_a.east_input_port= port_ab
        router_b.west_output_port= port_ab
        port_ab.setPort(router_a, router_b)

        port_ba= port()
        router_b.west_input_port= port_ba
        router_a.east_output_port= port_ba
        port_ab.setPort(router_b, router_a)

        port_bc= port()
        router_b.south_input_port= port_bc
        router_c.north_output_port= port_bc
        port_bc.setPort(router_b, router_c)

        port_cb= port()
        router_c.north_input_port= port_cb
        router_b.south_output_port= port_cb
        port_cb.setPort(router_c, router_b)

        port_cd= port()
        router_c.west_input_port= port_cd
        router_d.east_output_port= port_cd
        port_cd.setPort(router_c, router_d)

        port_dc= port()
        router_d.east_input_port= port_dc
        router_c.west_output_port= port_dc
        port_dc.setPort(router_d, router_c)

        port_da= port()
        router_d.north_input_port= port_da
        router_a.south_output_port= port_da
        port_da.setPort(router_d, router_a)

        port_ad= port()
        router_d.north_output_port= port_ad
        router_a.south_input_port= port_ad
        port_ad.setPort(router_a, router_d)
    
    def buff_check(self):
        if(router_a.pe_buffer[0]!=["0"*34]):
            dummy()
        if(router_a.south_buffer[0]!=["0"*34]):
            dummy()
        if(router_a.east_buffer[0]!=["0"*34]):
            dummy()
        if(router_b.pe_buffer[0]!=["0"*34]):
            dummy()
        if(router_b.west_buffer[0]!=["0"*34]):
            dummy()
        if(router_b.south_buffer[0]!=["0"*34]):
            dummy()
        if(router_c.pe_buffer[0]!=["0"*34]):
            dummy()
        if(router_c.west_buffer[0]!=["0"*34]):
            dummy()
        if(router_c.north_buffer[0]!=["0"*34]):
            dummy()
        if(router_d.pe_buffer[0]!=["0"*34]):
            dummy()
        if(router_d.north_buffer[0]!=["0"*34]):
            dummy()
        if(router_d.east_buffer[0]!=["0"*34]):
            dummy()

    def dummy(self):
        return "Actions bhay router wale"

    def readInp(self, s):

        return "ehhe"