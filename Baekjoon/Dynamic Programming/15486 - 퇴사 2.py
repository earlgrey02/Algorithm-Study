import sys

input = sys.stdin.readline

n = int(input())
times = [0] + [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] + [0 for _ in range(n + 1)]

temp = 0
for i in range(1, n + 1):
    temp = max(temp, dp[i])
    if i + times[i][0] <= n + 1:
        dp[i + times[i][0]] = max(temp + times[i][1], dp[i + times[i][0]])

print(max(dp))