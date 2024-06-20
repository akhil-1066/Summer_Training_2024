coins = list(map(int, input().split()))
amount = int(input())
dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
for i in range(len(coins) + 1):
    dp[i][0] = 1
for i in range(1, len(coins) + 1):
    for j in range(1, amount + 1):
        if  j >= coins[i - 1]:
            dp[i][j] = max(dp[i - 1][j - coins[i - 1]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print('Possible' if dp[-1][-1] else 'Not Possible')