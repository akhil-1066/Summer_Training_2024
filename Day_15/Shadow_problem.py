l = list(map(int, input().split()))
maxl = maxr = float('-inf')
am = pm = 0
for num in l:
    if num > maxl:
        maxl = num
        am += 1
for num in l[::-1]:
    if num > maxr:
        maxr = num
        pm += 1
print(am, pm)