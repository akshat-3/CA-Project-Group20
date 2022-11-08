import fileinput
import Clock
import Packet
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

for line in input:
    source = line[1]
    dest = line[2]
    injectCycle = line[0]
    payload = line[3]
    packet = Packet.Packet(payload, source, dest, injectCycle)
    print(packet.flit())
