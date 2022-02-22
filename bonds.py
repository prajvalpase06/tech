name1 = str(input("Enter first name: "))
name2 = str(input("Enter second name: "))
N = {}
string = name1 + " bonds " + name2
for i in string:
    if i==' ':
        continue
    if i in N:
        N[i] += 1
    else:
        N[i] = 1
print(type(N))