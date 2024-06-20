def Traverse(l):
    if not l:
        return 0
    prev2 = 0
    prev1 = l[0]
    for i in range(1, len(l)):
        current = max(prev1, prev2 + l[i])
        print(i,l[i],prev2, prev1,current)
        prev2 = prev1
        prev1 = current
    return prev1
l = list(map(int, input().split()))
print(Traverse(l))