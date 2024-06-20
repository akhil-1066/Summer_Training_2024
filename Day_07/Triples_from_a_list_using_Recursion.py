l = list(map(int,input().split()))
ans = []
def Triples(l, k):
    def fun(curr = [], start = 0):
        if len(curr) == k:
            print(curr)
            return
        for i in range(start, len(l)):
            fun(curr + [l[i]], i+1)
    fun()
Triples(l, 3)