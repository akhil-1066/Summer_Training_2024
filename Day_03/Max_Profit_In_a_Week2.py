l = list(map(int,input().split()))
max_profit = 0
max_price = float('-inf')
for i in range(len(l)-1, 0, -1):
    max_price = max(max_price, l[i])
    max_profit = max(max_profit, max_price - l[i])
print(max_profit)