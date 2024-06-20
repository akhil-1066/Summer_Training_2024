l = list(map(int,input().split()))
winner, count = l[0], 1
for num in l[1:]:
    if num != winner:
        count -= 1
        if not count:
            count = 1
            winner = num
    else:
        count += 1
if l.count(winner)>len(l)//2:
    print(winner)