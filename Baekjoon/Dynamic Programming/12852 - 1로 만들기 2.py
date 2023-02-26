import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
dp = [[] for _ in range(n + 1)]
dp[1] = [1]
if n >= 2:
    dp[2] = [1, 2]
if n >= 3:
    dp[3] = [1, 3]

for i in range(4, n + 1):
    dp[i] = dp[i - 1]
    if i % 3 == 0 and len(dp[i // 3]) < len(dp[i]):
        dp[i] = dp[i // 3]
    if i % 2 == 0 and len(dp[i // 2]) < len(dp[i]):
        dp[i] = dp[i // 2]
    dp[i] = dp[i] + [i]

print(len(dp[n]) - 1)
print(*dp[n][::-1])