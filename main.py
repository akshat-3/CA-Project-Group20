import fileinput
import Clock
import Packet
from Mesh import *

input = []

for line in fileinput.input(files='Input'):
    A = line.split(' ')
    for i in range(len(A)):
        j = A[i]
        if (j == '\n' or j == '\r'):
            A.remove(j)
        elif ('\r' in j):
            j = j[0:len(j)-2]
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

print(processed_input)
clk = Clock.Clock()
clk.startClock()
Mesh2D = Mesh()
i = 0
#assuming in order traffic only
while(1):
    if(i < len(processed_input) and int(processed_input[i][0])<=clk.count):
        print("Injecting packet at cycle: ",clk.count)
        for j in range(3,8):
            flag = 0
            if processed_input[i][j] != "0"*34:
                flag = Mesh2D.injectPacket(processed_input[i][j], j - 3, processed_input[i][1])
                if flag == 1:
                    print("Packet injected successfully\n")
                    processed_input[i][j] = "0"*34
                    break

                else:
                    print("Packet injection failed\n")
                    break
            elif (processed_input[i][7] == "0"*34):
                i+=1
                break
        
    Mesh2D.update()
    clk.updateCycle()

clk.stopClock()
