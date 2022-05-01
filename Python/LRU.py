print("Enter the number of frames: ", end="")
capacity = int(input())
f, st, fault, pf = [], [], 0, 'No'
print("Enter the page reference sequence: ", end="")
s = list(map(int, input().strip().split()))
print("\nString | Frame | Fault")
for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
            st.append(len(f) - 1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        pf = 'Yes'
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
        pf = 'No'
    print(" %d\t\t" % i, end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity - len(f)):
        print(' ', end=' ')
    print(" %s" % pf)
print(f"Total requests : {len(s)}")
print(f"Total Page Faults : {fault}")
