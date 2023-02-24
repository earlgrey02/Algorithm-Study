import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [100001 for _ in range(k + 1)]
dp[0] = 0

for i in coins:
    for j in range(1, k + 1):
        if j >= i:
            dp[j] = min(dp[j - i] + 1, dp[j])
            
print(dp[k] if dp[k] <= 100000 else -1)