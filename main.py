import fileinput
from Clock import *
import Packet
from Mesh import *

input = []

for line in fileinput.input(files='Input'):
    A = line.split(' ')
    for i in range(len(A)):
        j = A[i]
        if (j == '\n'):
            A.remove(j)
        elif ('\n' in j):
            j = j[0:len(j)-1]
            A[i] = j

    if (len(A[-1]) == 96):
        input.append(A)


processed_input = []

for line in input:
    injectCycle = line[0]
    source = line[1]
    dest = line[2]
    payload = line[3]
    packet = Packet.Packet(payload, source, dest, injectCycle)
    input_line = [injectCycle,source,dest]+packet.flit()
    processed_input.append(input_line)


clk = Clock()
clk.startClock()
Mesh2D = Mesh()

for data in processed_input:
    if(data[0]==clk.count):
        #inject data
        if(data[1]=="A"):
            pass
        if(data[1]=="B"):
            pass
        if(data[1]=="C"):
            pass
        if(data[1]=="D"):
            pass
    
    
    clk.updateCycle()


clk.stopClock()

print(processed_input)
