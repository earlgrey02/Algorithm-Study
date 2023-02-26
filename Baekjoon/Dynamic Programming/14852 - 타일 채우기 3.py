import sys

input = sys.stdin.readline

n = int(input())
dp = [[0, 0] for _ in range(n + 1)]
dp[0] = [1, 1]
if n >= 1:
    dp[1] = [2, 3]
if n >= 2:
    dp[2] = [7, 10]

for i in range(3, n + 1):
    dp[i][0] = (dp[i - 2][0] + dp[i - 1][1] * 2) % (10 ** 9 + 7)
    dp[i][1] = (dp[i - 1][1] + dp[i][0]) % (10 ** 9 + 7)

print(dp[n][0] % (10 ** 9 + 7))