import fileinput
import Clock
import Packet
from Mesh import *
import logging
import argparse

import signal
import sys

def signal_handler(sig, frame):
    print('\nSimulation Ended')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--traffic", help="Input Traffic File")
parser.add_argument("-r", "--routing", help="Routing Algorithm to use")

args = parser.parse_args()


logging.basicConfig(filename="Logfile.log", filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

input = []

for line in fileinput.input(files=args.traffic):
    A = line.split(' ')
    if (len(A) == 1) and (A[0] == '\n'):
        continue
    for i in range(len(A)):
        j = A[i]
        if (j == '\n' or j == '\r'):
            A.remove(j)
        elif ('\r' in j or '\n' in j):
            j = j[0:len(j)-1]
            A[i] = j
    print(A)
    if (len(A[-1]) == 96):
        input.append(A)

processed_input = []
count = 0
for line in input:
    #print(count)
    injectCycle = line[0]
    source = line[1]
    dest = line[2]
    payload = line[3]
    packet = Packet.Packet(payload, source, dest, injectCycle,count)
    input_line = [injectCycle,source,dest]+packet.flit()
    processed_input.append(input_line)
    count+=1

clk = Clock.Clock()
clk.startClock()
Mesh2D = Mesh()
i = 0
open('Logfile.log', 'w').close()
addition_flag = 0
#assuming in order traffic only
print("Simulation Started. Press Ctrl+C to stop")
while(1):
    if(i < len(processed_input) and int(processed_input[i][0])<=clk.count):
        for j in range(3,8):
            flag = 0
            if processed_input[i][j] != "0"*34:
                flag = Mesh2D.injectPacket(processed_input[i][j], j - 3, processed_input[i][1])
                if flag == 1:
                    logger.info('Router: ' + processed_input[i][1] + " Received from PE at clock cycle: "+ str(clk.count) +' Flit received: '+ processed_input[i][j])
                    processed_input[i][j] = "0"*34
                    addition_flag = 1
                    break
                else:
                    break
            elif (processed_input[i][7] == "0"*34):
                i+=1
                break
    # else:
    #     print('hello')    
    value = Mesh2D.update(clk.count, args.routing)
    if value >= 0:
        clk.updateCycle()

clk.stopClock()