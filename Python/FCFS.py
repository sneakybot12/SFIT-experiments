num = int(input("Enter no. of processes: "))
d = dict()

for i in range(num):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process "+str(i+1)+": "))
    b = int(input("Enter burst time of process "+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l
print("val of d ", d)
d = sorted(d.items(), key=lambda item: item[1][0])

ET = []
for i in range(len(d)):
    if i == 0:
        ET.append(d[i][1][1])

    else:
        ET.append(ET[i - 1] + d[i][1][1])

TAT = []
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])

WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])

AWT = 0
for i in WT:
    AWT += i
AWT = (AWT/num)

ATAT = 0
for i in TAT:
    ATAT += i
ATAT = (ATAT/num)

print(" Process | AT  |  BT  |  ET  | TAT  | WT  |")
for i in range(num):
    print("    ", d[i][0], " | ", d[i][1][0], " | ", d[i][1][1], " | ", ET[i], " | ", TAT[i], " | ", WT[i], " | ")
print("Average Waiting Time: ", AWT)
print("Average Turn around Time: ", ATAT)
