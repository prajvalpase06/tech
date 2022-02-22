import numpy as np

name1 = str(input("Enter first name: "))
name2 = str(input("Enter second name: "))
N = {}
newCounts = []
string = name1 + " bonds " + name2
for i in string:
    if i == ' ':                                                #if space is encountered, skip and dont count ' '
        continue                                            
    if i in N:                                                 # get the occurences of each letter.
        N[i] += 1
    else:
        N[i] = 1
counts = list(N.values())                                       #create a list of values of dict
z = int(len(counts) / 2)
for x in range(z):                                                          
    newCounts.append(counts[x] + counts[-1 - x])                #counts [x] is current position, and counts [-1-x] gives us last, second last position... etc
if (len(counts) % 2) != 0:
    newCounts.insert(len(counts), counts[z])
bonds = np.array(newCounts)
mid = int(len(newCounts)/2)
for ele in range(mid):
    bonds[ele] = bonds[ele] + bonds[-1-ele] 
if (len(newCounts) % 2 != 0):
    bonds[-1] = bonds[mid]
print(bonds)
