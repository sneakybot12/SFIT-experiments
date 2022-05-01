wt = []
bt = []
at = []
tat = []
proc = []

n = int(input("Enter no. of proc: "))
quantum = int(input("Enter Quantum : "))

for i in range(n):
    a = int(input("Enter arrival time of process "+str(i+1)+": "))
    b = int(input("Enter burst time of process "+str(i+1)+": "))
    p = str(i + 1)
    at.append(a)
    bt.append(b)
    proc.append(p)

print(at)
print(bt)


def findWT(processes, n, bt, wt, quantum):

    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0

    while (1):
        check = True

        for i in range(n):

            if (rem_bt[i] > 0):
                check = False

                if (rem_bt[i] > quantum):

                    t += quantum

                    rem_bt[i] -= quantum

                else:

                    t = t + rem_bt[i]

                    wt[i] = t - bt[i]

                    rem_bt[i] = 0
        # checker
        if (check == True):
            break


# TAT
def findTAT(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


# AWT + ATAT
def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    findWT(processes, n, bt, wt, quantum)
    findTAT(processes, n, bt, wt, tat)

    # Display
    print("Processes    Arrival Time    Burst Time     Waiting Time    Turn-Around Time")

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", proc[i], "\t\t\t", at[i], "\t\t\t\t", bt[i], "\t\t\t\t", wt[i], "\t\t\t\t", tat[i])

    print("\nAverage waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = %.5f " % (total_tat / n))
findavgTime(proc, n, bt, quantum)
