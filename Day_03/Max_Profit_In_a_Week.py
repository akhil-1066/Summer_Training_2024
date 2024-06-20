l = list(map(int,input().split()))
max_list = [0] * (len(l))
max_list[-1] = l[-1]
for i in range(len(l)-2, 0,-1):
    max_list[i] = max(max_list[i+1], l[i])
max_profit = 0
for i in range(len(l)-1):
    max_profit = max(max_profit, max_list[i+1] - l[i])
print(max_profit)