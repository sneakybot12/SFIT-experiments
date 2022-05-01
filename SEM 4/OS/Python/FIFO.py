print("Enter the number of frames: ", end="")
capacity = int(input())
f, fault, top, pf = [], 0, 0, 'No'
print("Enter the page reference sequence: ", end="")
s = list(map(int, input().strip().split()))
print("\nString | Frame | Fault")
for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top + 1) % capacity
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'
    print(" %d\t\t" % i, end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity - len(f)):
        print(' ', end=' ')
    print(" %s" % pf)
print(f"Total requests : {len(s)}")
print(f"Total Page Faults : {fault}")
