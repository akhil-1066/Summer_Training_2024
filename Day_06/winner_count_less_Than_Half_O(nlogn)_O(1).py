l = list(map(int,input().split()))
l.sort()
length = max_len = 1
for i in range(1,len(l)):
    if l[i] == l[i-1]:
        length += 1
        continue
    if length>max_len:
        max_len = length
        num = l[i-1]
    length = 1
if length>max_len:
        max_len = length
        num = l[-1]
if max_len>len(l)//2:
    print(num)