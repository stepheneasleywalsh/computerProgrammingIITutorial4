# THIS IS MY ANSWER ONLY
# THERE ARE OTHER THINGS YOU COULD ADD TO MAKE IT
# BETTER BUT THIS IS A MINIMUM WORKING PROGRAM
# SO I AM HAPPY WITH IT

import csv
import matplotlib.pyplot as plt
import os

# First ask for the file name of voltages
V = input("Filename of the voltages: ")
if os.path.exists(V+".csv"):
    V = V + ".csv"
while not os.path.exists(V):
    print("Oh, sorry I can't find that file, try again")
    V = input("Filename of the voltages: ")
    if os.path.exists(V + ".csv"):
        V = V + ".csv"

# Second ask for the file name of currents
I = input("Filename of the currents: ")
if os.path.exists(I+".csv"):
    I = I + ".csv"
while not os.path.exists(V):
    print("Oh, sorry I can't find that file, try again")
    I = input("Filename of the voltages: ")
    if os.path.exists(I + ".csv"):
        I = I + ".csv"

# Open the voltages
with open(V, encoding="utf-8-sig") as f:
    readFile = csv.reader(f)
    voltages = []
    time = []
    skip = True
    for line in readFile:
        if skip:
            skip = False
        else:
            time.append(int(line[0]))
            voltages.append(int(line[1]))

# Open the currents
with open(I, encoding="utf-8-sig") as f:
    readFile = csv.reader(f)
    currents = []
    time = []
    skip = True
    for line in readFile:
        if skip:
            skip = False
        else:
            time.append(int(line[0]))
            currents.append(int(line[1]))

# Calculate the power
powers = []
for n in range(0,len(time)):
    p = voltages[n]*currents[n]
    powers.append(p)

# Graph
plt.plot(time,powers)
plt.title("Power Vs Time")
plt.xlabel("Time / ms")
plt.ylabel("Power / W")
plt.axhline(color="red")
plt.axvline(color="red")
plt.show()

# Calculate the average power
print("Average Power:", sum(powers)/len(powers),"W")
