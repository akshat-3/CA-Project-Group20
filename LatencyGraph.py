import fileinput
import numpy as np
import matplotlib.pyplot as plt
 
  
data = {}

filename = "Logfile.log"
index = 0
min = 10
lines=[]
for line in fileinput.input(filename):
    lines.append(line)

for line in lines:
    A = line.split(' ')
    flit = A[-1]
    if flit[32:34] == "00" or flit[32:34] == "11":
        packet_id = int(flit[0:28],2)
        #print(packet_id)

        if packet_id not in data:
            start_clock = int(A[8])
            end_clock = 0
            for line1 in lines:
                A1 = line1.split(' ')
                flit1 = A1[-1]
                if int(flit1[0:28],2) == packet_id:
                    end_clock = int(A1[8])
            data[packet_id] = max(end_clock-start_clock+1,min)
    index += 1


packets = list(data.keys())
latency = list(data.values())
plt.plot(packets, latency) 
plt.scatter(packets, latency)
plt.xlabel("Packet ID")
plt.ylabel("Latency")
plt.show()