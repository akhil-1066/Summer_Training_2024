l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
n1, n2 = len(l1), len(l2)
l = []
i = j = 0
while i<n1 and j<n2:
    if l1[i]<l2[j]:
        l.append(l1[i])
        i+=1
    else:
        l.append(l2[j])
        j+=1
l += l1[i:] + l2[j:]
print(l)