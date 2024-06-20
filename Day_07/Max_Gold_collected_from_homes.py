l = list(map(int,input().split()))
def Traverse(l, s = 0):
    if not l:
        return s
    if len(l)==1:
        return s + l[0]
    return max(Traverse(l[2:], s + l[0]), Traverse(l[3:], s + l[1]))
print(Traverse(l))