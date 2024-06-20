coins = list(map(int,input().split()))
amount = int(input())
def change(coins, money = 0, coin_count = 0):
    if money == amount:
        return coin_count
    if money > amount or not coins:
        return float('inf')
    i = 0
    minn = float('inf')
    while i <= (amount - money)//coins[0]:
        res = change(coins[1:], money + coins[0] * i, coin_count + i)
        minn = min(minn, res)
        i += 1
    return minn
ans = change(coins)
print(-1 if ans == float('inf') else ans)