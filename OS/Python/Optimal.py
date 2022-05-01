print("Enter the number of frames: ", end="")
capacity = int(input())
f, fault, pf = [], 0, 'No'
print("Enter the page reference sequence: ", end="")
s = list(map(int, input().strip().split()))
print("\nString | Frame | Fault")
occurance = [None for i in range(capacity)]
for i in range(len(s)):
    if s[i] not in f:
        if len(f) < capacity:
            f.append(s[i])
        else:
            for x in range(len(f)):
                if f[x] not in s[i + 1:]:
                    f[x] = s[i]
                    break
                else:
                    occurance[x] = s[i + 1:].index(f[x])
            else:
                f[occurance.index(max(occurance))] = s[i]
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'
    print(" %d\t\t" % s[i], end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity - len(f)):
        print(' ', end=' ')
    print(" %s" % pf)
print(f"Total requests : {len(s)}")
print(f"Total Page Faults : {fault}")
