from collections import defaultdict
dict = defaultdict(int)
l = list(map(int,input().split()))
for i in l:
    dict[i] += 1
for i in dict:
    print(i,'-',dict[i])