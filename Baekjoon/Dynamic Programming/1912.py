import sys

input = sys.stdin.readline

n = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(2, n + 1):
    if dp[i - 1] >= 0:
        dp[i] += dp[i - 1]

print(max(dp[1:]))