coins = list(map(int,input().split()))
amount = int(input())
n=len(coins)
dp=[[float('inf') for _ in range(amount+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=0
for i in range(1,n+1):
    for j in range(1,amount+1):
        if coins[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i-1]]+1)
#print(*dp,sep='\n')
print(-1 if dp[n][amount]==float('inf') else dp[n][amount])