# Read Me
## Working
We take the input from a text file, and divide the packets into flits for transmission. Then we instantiated the clock and mesh classes. In the mesh class we instantiated 4  routers. And in each router we have 10 ports, 5(North, South, East, West, PE) for input and 5 for output and we have an infinite buffer.

Each router has it's own processing element which feeds it the input. Then we have instantiated a crossbar connects every input to every output of an NoC.

Then using the established connections transmission of flits start to take place.


## Graph Plotter
### For the first plot
We have created 8 counters so as to keep a count of how many flits have passed through each connection.
```python
data= {'A-PE':0, 'B-PE':0, 'C-PE':0,'C-D':0,
'A-B':0, 'B-C':0, 'C-D':0,'D-A':0}
```

In the output file we have mentioned the source and destination of the flit. So, using them we update the 8 counters and simply plot a bar graph using matplotlib.

### For the second plot
We had 28 filler bits in the header flit and 32 filler bits in the tail flit. So, we used them to keep a track of the packet ID. Then, using the log we found the first and last occurance of the packet, and calculated the latencies.

Lastly we plotted the latency per packet using matplotlib.

## Usage Instructions
### Command to run the code

```bash
# execution code
python3 main.py -t <Input file name> -r <Routing Algorithm>

# example
python3 main.py -t input.txt -r YX
```

### Command to plot the graphs
```python
# for the latency graph
python3 LatencyGraph.py

# for the LinkCount graph
python3 LinkGraph.py
```

## Members
Akshansh Jaiswal: 2020018


Akshat Saini: 2020019


Nakul Thureja: 2020528


Shubham Das: 2020245