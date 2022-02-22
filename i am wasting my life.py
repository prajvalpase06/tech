import numpy as np

name1 = str(input("Enter first name: "))
name2 = str(input("Enter second name: "))
N = {}
newCounts = []
string = name1 + " bonds " + name2
for i in string:
    if i == ' ':
        continue
    if i in N:
        N[i] += 1
    else:
        N[i] = 1
counts = list(N.values())
print(counts)
z = int(len(counts) / 2)
for x in range(z):
    newCounts.append(counts[x] + counts[-1 - x])
if (len(counts) % 2) != 0:
    newCounts.insert(len(counts), counts[z])
bonds = np.array(newCounts)
mid = int(len(newCounts)/2)
for ele in range(mid):
    bonds[ele] = bonds[ele] + bonds[-1-ele] 
if (len(newCounts) % 2 != 0):
    bonds[-1] = bonds[mid]

