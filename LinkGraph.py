import fileinput

import numpy as np
import matplotlib.pyplot as plt
 
  
data = {'A-PE':0, 'B-PE':0, 'C-PE':0,'C-D':0,
        'A-B':0, 'B-C':0, 'C-D':0,'D-A':0}

filename = "Logfile.log"

for line in fileinput.input(filename):
    A = line.split(' ')
    field1 = A[1]+"-"+A[4]
    field2 = A[4]+"-"+A[1]
    print(field1 + " " + field2)
    if field1 in data:
        data[field1] = data[field1] + 1
    elif field2 in data:
        data[field2] = data[field2] + 1

print(data)  
my_keys = list(data.keys())
my_values = list(data.values())
  
# fig = plt.figure(figsize = (10, 5))
 
# # creating the bar plot
plt.bar(my_keys, my_values)
 
plt.xlabel("Connection")
plt.ylabel("No. of flits sent over a connection")
plt.show()