coins = list(map(int,input().split()))
amount = int(input())
n=len(coins)
dp=[float('inf')] * (amount+1)
dp[0]=0
for coin in coins:
    for j in range(1,amount+1):
        if coin<=j:
            dp[j] = min(dp[j], dp[j-coin] + 1)
#print(*dp,sep='\n')
print(-1 if dp[amount]==float('inf') else dp[amount])