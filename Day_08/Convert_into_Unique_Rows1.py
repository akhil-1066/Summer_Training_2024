from collections import Counter
l = list(map(int,input().split()))
counter = Counter(l)
#print(counter)
maxx = max(counter.values())
ans = [ [] for _ in range(maxx)]
for num in l[::-1]:
    ans[counter[num] - 1].append(num)
    counter[num] -= 1
print([subl[::-1] for subl in ans])