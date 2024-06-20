from collections import defaultdict
l = list(map(int,input().split()))
d = defaultdict(int)
for num in l:
    d[num] += 1
for num in d:
    if d[num]>len(l)//2:	
        print(d[num])