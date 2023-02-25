import sys

input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n + 1)]
dp[1] = [1 for _ in range(10)]

for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][:j + 1]) % 10007

print(sum(dp[n]) % 10007)