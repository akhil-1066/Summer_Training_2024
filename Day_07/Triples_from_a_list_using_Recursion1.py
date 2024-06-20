l = list(map(int,input().split()))
ans = []
def Triples(l1, l2, l3):
    if not (l1 and l2 and l3):
        return
    triple = (l1[0], l2[0], l3[0])
    if triple in ans:
        return
    ans.append(triple)
    Triples(l1, l2, l3[1:])
    Triples(l1, l2[1:], l3[1:])
    Triples(l1[1:], l2[1:], l3[1:])
Triples(l, l[1:], l[2:])