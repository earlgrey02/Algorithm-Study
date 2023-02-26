import sys

input = sys.stdin.readline

n = int(input())
dp = [0] + [list(map(int, input().split())) for _ in range(n)]

for i in range(2, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

print(min(dp[n]))