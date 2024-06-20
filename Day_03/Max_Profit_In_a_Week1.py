l = list(map(int,input().split()))
max_profit = 0
for i in range(len(l)-1):
    max_profit = max(max_profit,  max(l[i+1:])- l[i])
print(max_profit)