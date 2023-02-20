import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n + 1):
    for j in range(1, k + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % (10 ** 9)

print(dp[n][k])