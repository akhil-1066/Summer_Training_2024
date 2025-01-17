s1 = input()
s2 = input()
def longest_subsequence(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    ans = ''
    for i in range(m):
        if dp[-1][i] != dp[-1][i + 1]:
            ans += s2[i]
    return ans
print('Longest Common Subsequence:',longest_subsequence(s1, s2))