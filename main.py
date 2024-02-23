import os
import csv
import matplotlib.pyplot as p

while True:
    # Ask for file name
    file1 = input("Type in the name of the VOLT CSV file: ")
    file2 = input("Type in the name of the CURRENT CSV file: ")
    n = 0 # Counts the found files

    # Look for file1, add CSV to name if they don't type it
    if ".csv" in file1:
        if os.path.exists(file1):
            print("File Found")
            n += 1
    elif ".csv" not in file1:
        file1 = file1 + ".csv"
        if os.path.exists(file1):
            print("File Found (I added the CSV in)")
            n += 1

    # Look for file2, add CSV to name if they don't type it
    if ".csv" in file2:
        if os.path.exists(file1):
            print("File Found")
            n += 1
    elif ".csv" not in file2:
        file2 = file2 + ".csv"
        if os.path.exists(file1):
            print("File Found (I added the CSV in)")
            n += 1
    if n == 2:
        # Two files are found so break out of the loop
        print("Loading files....")
        break
    else:
        print("Try again, please use FULL PATH NAMES if the files are not local.")

# Read those files
t1 = []
V = []
t2 = []
I = []
with open(file1,encoding='utf-8-sig') as f1:
    csvRead1 = csv.reader(f1)
    for row in csvRead1:
        t1.append(row[0])
        V.append(row[1])
nameTime1 = t1.pop(0)
nameVolt = V.pop(0)

with open(file2,encoding='utf-8-sig') as f2:
    csvRead2 = csv.reader(f2)
    for row in csvRead2:
        t2.append(row[0])
        I.append(row[1])
nameTime2 = t2.pop(0)
nameCurrent = I.pop(0)

# Check Time is okay
if not nameTime1 == nameTime2:
    print("Error in files, time name not the same")
    quit()

if not t1 == t2:
    print("Error time stamps not the same")
    quit()

# Make the graph
P = []
n = 0
while True:
    try:
        P.append(float(V[n])*float(I[n]))
        n+= 1
    except:
        break

# Graph
xValues = t1
yValues = P
p.title("Power Graph")
p.xlabel(nameTime1)
p.ylabel("Watts")
p.plot(xValues,yValues, linestyle="dotted", color="red", linewidth="2")
p.grid()
p.axhline()
p.axvline()
p.show()

# Average Power
average = sum(P)/len(P)
print("Average power is", average, "Watts")

quit()
