#Input:  l1 = 6 3 2 9 4 7
# 		 l2 = 8 7 5 3 6 9
#Output: [48, 32, 40]

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
n1, n2 = len(l1), len(l2)
ans = []
def match(i = 0, j = 0, summ = 0):
    #print(i,j)
    if i>=n1:
        return
    if j>=n1:
        ans.append(summ)
        match(i + 1, 0)
    elif not l1[i] & 1:
        if l2[j] & 1:
            summ += l1[i] + l2[j]
        match(i, j + 1, summ)
    else:
        if l2[j] & 1:
            match(i + 1, j, summ)
        else:
            match(i + 1, j + 1, summ)
match()
print(ans)