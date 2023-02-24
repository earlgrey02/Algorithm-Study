import sys

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)]
if n >= 2:
    dp[2] = 3
if n >= 4:
    dp[4] = 11

for i in range(6, n + 1, 2):
    dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2

print(dp[n])