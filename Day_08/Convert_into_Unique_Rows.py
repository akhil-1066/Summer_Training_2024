l = list(map(int,input().split()))
ans = [[]]
for num in l:
    for subl in ans:
        if num not in subl:
            subl.append(num)
            break
    else:
        ans.append([num])
print(ans)